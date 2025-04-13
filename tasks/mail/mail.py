
from typing import Dict
from zafkiel import logger, Timer
from tasks.mail.assets.assets_mail import * 
from tasks.base.page import page_mail
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE
from module.AetherGazerHelper import AetherGazerHelper
from module.Controller import Controller
from config import Config

class Mail(AetherGazerHelper):
    def __init__(self, config: Config, controller: Controller) -> None:
        super().__init__(config, controller)
        
    def check_mail(self):
        """
        检查邮件
        :return:
        """
        self.ui_ensure(page_mail)

        loop_timer = Timer(0, 5).start()
        while True:
            if loop_timer.reached(): 
                logger.critical("无邮件可领取或领取失败")
                return False
            
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, local_search=True, blind=True):
                logger.info("领取邮件奖励成功")
                break

            if self.find_click(MAIL_REWARD_CLICK, local_search=True, blind=True):
                logger.info("存在奖励邮件")
                continue

        return True

    def run(self):
        """
        邮件界面
        """
        self.check_mail()
        