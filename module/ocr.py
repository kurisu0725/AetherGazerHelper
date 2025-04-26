import re
from typing import List
from zafkiel.device.template import ImageTemplate
from zafkiel.ocr import Ocr, OcrResultButton
from zafkiel import logger
from zafkiel.utils import crop
from functools import cached_property
from pponnxcr.predict_system import BoxedResult

from cnocr import CnOcr
class BaseCnOcr(Ocr):

    def __init__(self, button: ImageTemplate, lang=None, name=None):
        """
        Args:
            button:
            lang: If None, use in-game language
            name: If None, use button.name
        """
        if lang is None:
            lang = 'cn'
        if name is None:
            name = button.name

        self.button: ImageTemplate = button
        self.lang: str = lang
        self.name: str = name

    @cached_property
    def model(self):
        return CnOcr()

    def results2boxedresult(self, results) -> List[OcrResultButton]:
        """
        Convert OCR results to OcrResultButton
        Args:
            results: OCR results
        Returns:
            List[OcrResultButton]
        """
        result = []
        for res in results:
            if isinstance(res, dict):
                text = res['text']
                area = res['area']
            else:
                text = res.text
                area = res.area

            button = OcrResultButton(
                name=self.name,
                text=text,
                area=area,
                lang=self.lang,
            )
            result.append(button)
        return result
    def ocr_common(self, image, keyword_class, direct_ocr=False):
        if not direct_ocr:
            image = crop(image, self.button.area)
        results = self.model.ocr(image)

        keyword_results = []
        for result in results:
            obj = keyword_class()
            setattr(obj, self.lang, result['text'])
            keyword_results.append(obj)
        logger.info(f"ocr_common results: {keyword_results}")
        return keyword_results

        

class GeneralOcr(Ocr):
    def __init__(self, button: ImageTemplate, lang='en', name=None):
        super().__init__(button, lang=lang, name=name)

    def after_process(self, result):
        result = super().after_process(result)
        logger.info(f"ocr result: {result}")
        # 识别错误
        result = result.replace('介质搜取', '介质攫取')

        return result


class DigitCounter(Ocr):
    def __init__(self, button: ImageTemplate, lang='en', name=None):
        super().__init__(button, lang=lang, name=name)

    def after_process(self, result):
        result = super().after_process(result)
        # remove empty chars,  to resolve case  `120 /120`, it will lead to ocr failed.
        result = result.replace(' ', '')
        if (len(result) == 4 or len(result) == 3)and result[1] == '1':
            result = result[:1] + '/' + result[2:]
        return result
    def format_result(self, result) -> tuple[int, int, int]:
        """
        Do OCR on a counter, such as `14/15`, and returns 14, 1, 15

        Returns:
            int:
        """
        result = self.after_process(result)
        
        logger.info(f"after process: {result}")

        res = re.search(r'(\d+)/(\d+)', result)
        if res:
            groups = [int(s) for s in res.groups()]
            current, total = int(groups[0]), int(groups[1])
            return current, total - current, total
        
        res = re.search(r'(\d+)1(\d+)', result)
        if res:
            groups = [int(s) for s in res.groups()]
            current, total = int(groups[0]), int(groups[1])
            return current, total - current, total
        else:
            # logger.warning(f'No digit counter found in {result}')
            return 0, 0, 0

if __name__ == "__main__":
    image = r"D:\VSCode_Workplace\Python\GF2_Exilium_Script\assets\daily\RESOURCE_SEARCH_BUTTON.png"
    ocr = BaseOcr()
    result = ocr.ocr_common(image)
    print(result)