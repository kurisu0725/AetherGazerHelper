
from typing import Dict
from module.AetherGazerHelper import AetherGazerHelper
from module.Controller import Controller
from tasks.base.page import page_dorm, page_dorm_nav_kitchen, page_dorm_nav_character
from tasks.base.assets.assets_share import BACK_BUTTON
from tasks.dorm.assets.assets_dorm import *
from zafkiel.exception import LoopError
from zafkiel import Timer, logger
from config import Config

class Dorm(AetherGazerHelper):

    def __init__(self, config: Config, controller: Controller):
        super().__init__(config, controller)

        self.check_and_connect_device()

    def claim_kitchen(self):
        """
        Claim kitchen resources.
        """
        self.ui_ensure(page_dorm_nav_kitchen)

        loop_timer = Timer(0, 10).start()
        while True:
            if loop_timer.reached():
                raise LoopError("Claim kitchen resources timed out.")
            
            if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, blind=True):
                logger.info("Assigned kitchen tasks.")
                break
            
            if self.find_click(DORM_NAV_KITCHEN_CURRENCY_CLAIM, DORM_NAV_KITCHEN_CURRENCY_CLAIM, blind=True):
                logger.info("Claimed kitchen resources.")
                continue

            if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN, DORM_NAV_KITCHEN_TASK_ASSIGN, blind=True):
                logger.info("Exit claim_kitchen tasks.")
                continue

        self.touch(BACK_BUTTON, blind=True)

    def train_characters(self):
        """
        Train characters in the dormitory.
        """
        self.ui_ensure(page_dorm_nav_character)
        # solution1: 滑动拼接图像，
        # solution2: 霍夫圆检测 + 图像匹配


    def run(self):
        """
        Main function to run the dormitory task.
        """
        self.ui_ensure(page_dorm)

        self.claim_kitchen()
        self.train_characters()