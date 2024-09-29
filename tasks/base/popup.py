from zafkiel import API, Template
from zafkiel.decorator import run_until_true
from zafkiel.ocr import Keyword
from zafkiel import logger
from tasks.base.assets.assets_popup import *


class PopupHandler(API):


    def handle_notice(self):
        """

        Returns: bool
            whether find notice and click notice

        """
        if self.exists(NOTICE_FLAG):
            logger.info("Dealing with ui_addtional: handle_notice()")
            self.touch(NOTICE_CLOSE, blind=True)
            logger.info("Handle_notice() complete")
            return True
        return False
        



popup_handler = PopupHandler()
popup_list = [popup_handler.handle_notice]


def main_function():
    from utils.test_program import run_as_admin
    from pathlib import Path
    import datetime
    run_as_admin()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    process_str = "少女前线2：追放"
    popup_handler.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
        
    popup_handler.handle_notice()

if __name__ == "__main__":
    main_function()