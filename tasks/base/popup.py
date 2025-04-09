from zafkiel import exists, touch
from zafkiel import logger
from tasks.base.assets.assets_popup import *
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE, BACK_BUTTON

def register_handler(func):
    func._is_handler = True
    return func

class PopupHandler:

    @register_handler
    def handle_check_in_reward(self):
        """
        Claim check-in reward.
        领取签到, 月卡奖励
        """
        if exists(GET_ITEM):
            logger.info("Dealing with ui_addtional: handle_check_in_reward()")
            while True:
                if exists(POPUP_CHECK_IN_REWARD_CHECK):
                    continue
                if exists(GET_ITEM):
                    touch(CLICK_TO_CONTINUE, blind=True)
                    continue
                break
            #领取奖励后仍会停留在签到界面, 需要点击其他区域退出
            if exists(POPUP_CHECK_IN_REWARD_CHECK):
                touch(BACK_BUTTON, blind=True)
            logger.info("Handle_notice() complete")
            return True
        return False

    @register_handler    
    def handle_activity(self):
        """
        处理每日第一次弹出的时装，活动界面
        """
        if exists(POPUP_ACTIVITY_CHECK):
            logger.info('Dealing with ui_addtional: handle_activty()')
            touch(POPUP_ACTIVITY_CLICK, blind=True)
            logger.info("Handle_activity() complete")
            return True
        return False

    @register_handler
    def handle_battle_pass(self):
        """
        Handle with popup battle pass.
        处理战令弹窗
        """
        if exists(POPUP_BATTLE_PASS_CHECK):
            logger.info('Dealing with ui_addtional: handle_battle_pass()')
            touch(BACK_BUTTON, blind=True)
            logger.info("Handle_battle_pass() complete")
            return True


popup_handler = PopupHandler()
popup_list = [
    getattr(popup_handler, name) 
    for name in dir(popup_handler) 
    if callable(getattr(popup_handler, name)) and hasattr(getattr(popup_handler, name), '_is_handler')
]

    

if __name__ == "__main__":
    # popup_handler.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
    popup_handler.handle_activity()
