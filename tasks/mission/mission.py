
from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from tasks.base.page import page_mission, page_store, page_main, page_store_supply
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE
from tasks.base.assets.assets_switch import MISSION_DAILY_SWITCH_ON, MISSION_DAILY_SWITCH_OFF, MISSION_WEEKLY_SWITCH_ON, MISSION_WEEKLY_SWITCH_OFF
from tasks.base.assets.assets_page import MAIN_TO_MISSION
from tasks.mission.assets.assets_mission import *

class Mission(AetherGazerHelper):

    def __init__(self, config : Dict) -> None:
        super().__init__(config)

    def check_mission(self):
        """
        Check the mission status.
        检查任务状态
        """
        logger.info('正在尝试领取任务奖励.')
        self.ui_ensure(page_mission, MISSION_DAILY_SWITCH_ON)

        loop_timer = Timer(0, 3).start()
        rewardClaimed = False
        while True:
            if loop_timer.reached():
                if rewardClaimed:
                    logger.info("任务奖励领取完成.")
                else:
                    logger.error("任务领取超时.请检查是否有奖励可以领取或今日已领取过奖励.")
                break
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, blind=True):
                logger.info("领取奖励成功.")
                rewardClaimed = True
                continue
            if self.find_click(MISSION_DAILY_CLAIM, MISSION_DAILY_CLAIM):
                logger.info("领取每日任务奖励.")
            self.ui_goto(page_mission, MISSION_WEEKLY_SWITCH_ON)
            logger.info("切换至每周任务")
            if self.find_click(MISSION_WEEKLY_CLAIM, MISSION_WEEKLY_CLAIM):
                logger.info("领取每周任务奖励.")
            
    def test_mission(self):
        if self.find_click(MISSION_WEEKLY_SWITCH_OFF, MISSION_WEEKLY_SWITCH_OFF):
            logger.info("切换每周任务奖励.")



    def run(self):
        from utils.logger_func import task_info
        task_info('Mission')

        self.connect_device()
        self.check_mission()
        # self.test_mission()