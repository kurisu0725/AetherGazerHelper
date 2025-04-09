
from typing import Dict
from module.AetherGazerHelper import AetherGazerHelper
from module.Controller import Controller
from tasks.base.page import page_dorm, page_dorm_nav_kitchen
from tasks.dorm.assets.assets_dorm import *
from zafkiel.exception import LoopError
from zafkiel import Timer, logger

class Dorm(AetherGazerHelper):

    def __init__(self, config: Dict = None, controller: Controller = None):
        super().__init__(config, controller)

    def claim_kitchen(self):
        """
        Claim kitchen resources.
        """
        self.ui_ensure(page_dorm_nav_kitchen)

        loop_timer = Timer(0, 10).start()
        while True:
            if loop_timer.reached():
                raise LoopError("Claim kitchen resources timed out.")
            
            if self.find_click(DORM_NAV_KITCHEN_CURRENCY_CLAIM, DORM_NAV_KITCHEN_CURRENCY_CLAIM, blind=True):
                logger.info("Claimed kitchen resources.")
                continue
            
            if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN, DORM_NAV_KITCHEN_TASK_ASSIGN, blind=True):
                if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, blind=True):
                    logger.info("Assigned kitchen tasks.")
                else:
                    logger.warning("Failed to assign kitchen tasks.")
                logger.info("Exit claim_kitchen tasks.")
                break

    def train_characters(self):
        """
        Train characters in the dormitory.
        """
        

    def run(self):
        """
        Main function to run the dormitory task.
        """
        self.ui_ensure(page_dorm)

        self.claim_kitchen()
        self.train_characters()