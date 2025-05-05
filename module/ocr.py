import re
import numpy as np
from typing import List
from functools import cached_property
from pponnxcr.predict_system import BoxedResult

from zafkiel.device.template import ImageTemplate
from zafkiel.ocr import Ocr, OcrResultButton
from zafkiel import logger
from zafkiel.utils import crop
from zafkiel.exception import ScriptError
from cnocr import CnOcr


class BaseCnOcr(Ocr):

    def __init__(self, button: ImageTemplate, lang=None, name=None):
        """
        Args:
            button:
            lang: If None, use in-game language
            name: If None, use button.name
        """
        super().__init__(button, lang=lang, name=name)

    @cached_property
    def model(self):
        return CnOcr()

    # def _match_result(
    #     self,
    #     result,
    #     keyword_classes,
    #     lang: str = None,
    #     ignore_punctuation=True,
    #     ignore_digit=True,
    # ):
    #     """
    #     Args:
    #         result (str):
    #         keyword_classes: A list of `Keyword` class or classes inherited `Keyword`

    #     Returns:
    #         If matched, return `Keyword` object or objects inherited `Keyword`
    #         If not match, return None
    #     """
    #     if not isinstance(keyword_classes, list):
    #         keyword_classes = [keyword_classes]

    #     # Digits will be considered as the index of keyword
    #     if ignore_digit:
    #         if result.isdigit():
    #             return None

    #     # Try in current lang
    #     for keyword_class in keyword_classes:
    #         try:
    #             matched = keyword_class.find(
    #                 result,
    #                 lang=lang,
    #                 ignore_punctuation=ignore_punctuation
    #             )
    #             return matched
    #         except ScriptError:
    #             continue

    #     return None

    # def _product_button(
    #         self,
    #         boxed_result: BoxedResult,
    #         keyword_classes,
    #         lang: str = None,
    #         ignore_punctuation=True,
    #         ignore_digit=True
    # ) -> OcrResultButton:
    #     if not isinstance(keyword_classes, list):
    #         keyword_classes = [keyword_classes]

    #     matched_keyword = self._match_result(
    #         boxed_result.text,
    #         keyword_classes=keyword_classes,
    #         lang=lang,
    #         ignore_punctuation=ignore_punctuation,
    #         ignore_digit=ignore_digit,
    #     )
    #     button = OcrResultButton(boxed_result, matched_keyword)
    #     return button

    def results2boxedresult(self, results, image, keyword_class) -> List[OcrResultButton]:
        """
        Convert OCR results to OcrResultButton
        Args:
            results: OCR results
        Returns:
            List[OcrResultButton]
        """
        boxedresults = []
        for res in results:
            offset = np.array(self.button.area[:2], dtype=np.int32)
            res['position'] += offset
            area = *res['position'][0], *res['position'][2]
            img_crop = crop(image, area)
            boxresult = BoxedResult(box=area, img=img_crop, text=res['text'], score=res['score'])
            button = self._product_button(boxed_result=boxresult, keyword_classes=keyword_class, lang=self.lang)
            boxedresults.append(button)
        return boxedresults

    def ocr_common(self, image, keyword_class, direct_ocr=False):
        if not direct_ocr:
            image = crop(image, self.button.area)
        results = self.model.ocr(image)
        result_button = self.results2boxedresult(results, image, keyword_class)

        return result_button


class DigitCounter(Ocr):
    def __init__(self, button: ImageTemplate, lang='en', name=None):
        super().__init__(button, lang=lang, name=name)

    def after_process(self, result):
        result = super().after_process(result)
        # remove empty chars,  to resolve case  `120 /120`, it will lead to ocr failed.
        result = result.replace(' ', '')
        if (len(result) == 4 or len(result) == 3) and result[1] == '1':
            result = result[:1] + '/' + result[2:]
        return result

    def format_result(self, result) -> tuple[int, int, int]:
        """
        Do OCR on a counter, such as `14/15`, and returns 14, 1, 15

        Returns:
            int:
        """
        result = self.after_process(result)
        
        logger.debug(f"after process: {result}")

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
            logger.warning(f'No digit counter found in {result}')
            return 0, 0, 0


if __name__ == "__main__":
    image = r"D:\VSCode_Workplace\Python\GF2_Exilium_Script\assets\daily\RESOURCE_SEARCH_BUTTON.png"
    ocr = BaseCnOcr()
    result = ocr.ocr_common(image)
    print(result)
