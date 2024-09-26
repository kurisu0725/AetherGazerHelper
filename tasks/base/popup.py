from zafkiel import API, Template
from zafkiel.decorator import run_until_true
from zafkiel.ocr import Keyword

class PopupHandler(API):

    @run_until_true
    def handle_notice(self):
        return False



popup_handler = PopupHandler()
popup_list = [popup_handler.handle_notice]