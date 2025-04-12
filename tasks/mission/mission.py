
from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from tasks.base.page import page_mission, page_battle_pass, page_battle_pass_mission
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE
from tasks.base.assets.assets_switch import MISSION_DAILY_SWITCH_ON, MISSION_DAILY_SWITCH_OFF, MISSION_WEEKLY_SWITCH_ON, MISSION_WEEKLY_SWITCH_OFF
from tasks.base.assets.assets_page import MAIN_TO_MISSION
from tasks.mission.assets.assets_mission import *
from module.Controller import Controller

class Mission(AetherGazerHelper):

    def __init__(self, config : Dict, controller: Controller) -> None:
        super().__init__(config, controller)

    def check_mission(self):
        """
        Check the mission status.
        检查任务状态
        """
        logger.info('Trying claim daily mission rewards.')
        self.ui_ensure(page_mission, MISSION_DAILY_SWITCH_ON)

        loop_timer = Timer(5).start()
        rewardClaimed = False
        while True:
            if loop_timer.reached():
                if rewardClaimed:
                    logger.info("任务奖励领取完成.")
                else:
                    logger.error("任务领取超时.请检查是否有奖励可以领取或今日已领取过奖励.")
                break
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, blind=True):
                logger.info("Get rewards.")
                rewardClaimed = True
                continue
            if self.find_click(MISSION_DAILY_CLAIM, MISSION_DAILY_CLAIM):
                logger.info("Claim daily mission rewards complete.")
            self.ui_goto(page_mission, MISSION_WEEKLY_SWITCH_ON)
            logger.info("Switch to weekly mission page.")
            if self.find_click(MISSION_WEEKLY_CLAIM, MISSION_WEEKLY_CLAIM):
                logger.info("Claim weekly mission rewards complete.")
    
    def claim_battle_pass(self):
        """
        Claim battle pass rewards.
        战令/通行证奖励
        """
        self.ui_ensure(page_battle_pass)
        self.ui_goto(page_battle_pass_mission)
        
        logger.info("Trying to claim battle pass rewards.")
        
        if self.find_click(BATTLE_PASS_MISSION_CLAIM_ALL_CLICK, BATTLE_PASS_MISSION_CLAIM_ALL_CLICK, blind=True):
            logger.info("Claim battle pass mission rewards.")
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, blind=True):
                logger.info("Claim battle pass mission rewards complete.")
                
        else:
            logger.info("No battle pass mission rewards to claim.")
            
        self.ui_goto(page_battle_pass)
        if self.find_click(BATTLE_PASS_CLAIM_ALL_CLICK, BATTLE_PASS_CLAIM_ALL_CLICK, blind=True):
            logger.info("Claim battle pass rewards.")
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, blind=True):
                logger.info("Claim battle pass rewards complete.")
            else:
                logger.info("No battle pass rewards to claim.")
        else:
            logger.info("No battle pass rewards to claim.")
                

    def test_mission(self):
        if self.find_click(MISSION_WEEKLY_SWITCH_OFF, MISSION_WEEKLY_SWITCH_OFF):
            logger.info("切换每周任务奖励.")



    def run(self):
        from utils.logger_func import task_info
        task_info('Mission')

        # self.check_mission()
        self.claim_battle_pass()
        