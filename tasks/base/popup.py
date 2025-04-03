from zafkiel import API, Template
from zafkiel.decorator import run_until_true
from zafkiel.ocr import Keyword
from zafkiel import logger
from tasks.base.assets.assets_popup import *
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE

class PopupHandler(API):


    def handle_check_in_reward(self):
        """
        领取签到奖励
        Returns: bool

        """
        if self.exists(GET_ITEM):
            logger.info("Dealing with ui_addtional: handle_check_in_reward()")
            while True:
                if self.exists(POPUP_CHECK_IN_REWARD_CHECK):
                    continue
                if self.exists(GET_ITEM):
                    self.touch(CLICK_TO_CONTINUE, blind=True)
                    continue
                break
            #领取奖励后仍会停留在签到界面
            if self.exists(POPUP_CHECK_IN_REWARD_CHECK, blind=False):
                self.touch(CLICK_TO_CONTINUE, blind=False)
            logger.info("Handle_notice() complete")
            return True
        return False
        
    def handle_activity(self):
        """
        处理每日第一次弹出的时装，活动界面
        """
        if self.exists(POPUP_ACTIVITY_CHECK):
            logger.info('Dealing with ui_addtional: handle_activty()')
            self.touch(POPUP_ACTIVITY_CLICK, blind=True)
            logger.info("Handle_activity() complete")
            return True
        return False

popup_handler = PopupHandler()
popup_list = [popup_handler.handle_check_in_reward, popup_handler.handle_activity]


def main_function():
    from utils.test_program import run_as_admin
    from pathlib import Path
    import datetime
    run_as_admin()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    process_str = "少女前线2：追放"
    

if __name__ == "__main__":
    main_function()
    # popup_handler.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
    # popup_handler.handle_notice()