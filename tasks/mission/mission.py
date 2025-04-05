
from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from tasks.base.page import page_mission, page_store, page_main, page_store_supply
from tasks.base.assets.assets_share import BACK_BUTTON_2, BACK_TO_MAIN
from tasks.base.assets.assets_switch import MISSION_DAILY_SWITCH_ON, MISSION_DAILY_SWITCH_OFF, MISSION_WEEKLY_SWITCH_ON, MISSION_WEEKLY_SWITCH_OFF

class Mission(AetherGazerHelper):

    def __init__(self, config : Dict) -> None:
        super().__init__(config)

    def check_mission(self):
        """
        Check the mission status.
        检查任务状态
        """
        logger.info('正在尝试领取任务奖励.')
        # self.ui_ensure(page_mission, MISSION_DAILY_SWITCH_ON)

        # self.ui_goto(page_mission, MISSION_DAILY_SWITCH_ON)
        self.ui_ensure(page_main)

        # loop_timer = Timer(0, 10).start()
        # while True:
        #     if loop_timer.reached():
        #         raise LoopError('The operation has looped too many times')
            
            




    def run(self):
        from utils.logger_func import task_info
        task_info('Mission')

        self.connect_device()
        self.check_mission()