import re
from zafkiel.device.template import ImageTemplate
from zafkiel.ocr import Ocr
from zafkiel import logger

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