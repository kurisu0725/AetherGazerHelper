import datetime
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from tasks.mimir.assets.assets_mimir import *
from tasks.base.page import page_mimir, page_mimi_observation
from module.Controller import Controller
from utils.utils import get_current_weekday_and_time
class Mimir(AetherGazerHelper):
    def __init__(self, config: Dict, controller : Controller) -> None:
        super().__init__(config, controller)


    def check_mimi_observation_rewards(self) -> bool:
        now = datetime.datetime.now()
        weekday_num = now.weekday()
        current_time = now.time()
        five_am = datetime.time(5, 0, 0)  # 5:00 AM

        if weekday_num == 0:
            return current_time >= five_am
        elif weekday_num == 6:
            return True
        elif weekday_num == 0:
            return current_time < five_am
        else:
            return False

    def mimi_observation(self):
        """
        弥弥观测站
        """
        self.ui_goto(page_mimi_observation)
        logger.info("Trying to claim mimi observation rewards.")
        loop_timer = Timer(0, 10).start()
        redispatched = False
        while True:
            if redispatched:
                logger.info("Redispatch complete.")
                break

            if loop_timer.reached():
                logger.error("Mimi observation check timed out.")
                break

            if self.find_click(MIMI_OBSERVATION_DISPATCH, MIMI_OBSERVATION_DISPATCH, local_search=True):
                redispatched = True
                logger.info("Redispatch complete.")
                break

            if self.exists(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK, local_search=True):
                self.touch(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK, blind=True)
                while(self.exists(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK, local_search=True)):
                    self.touch(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK, blind=True)
                logger.info("Mimi observation exploration complete.")
                continue

            if self.find_click(MIMI_OBSERVATION_CLAIM_ALL, MIMI_OBSERVATION_CLAIM_ALL, local_search=True):
                logger.info("Mimi observation claim all complete.")
                continue
        # TODO: 周期奖励添加  
        if self.check_mimi_observation_rewards():
            pass
    
    def test_mimir(self):
        """
        测试函数
        """
        from tasks.base.page import MAIN_TO_MIMIR
        if self.find_click(MAIN_TO_MIMIR, MAIN_TO_MIMIR):
            logger.info("进入弥弥尔")


    def run(self):
        """
        运行函数
        """
        from utils.logger_func import task_info
        task_info('Mimir')

        self.ui_ensure(page_mimir)
        self.mimi_observation()