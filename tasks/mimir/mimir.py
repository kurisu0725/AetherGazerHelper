
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from tasks.mimir.assets.assets_mimir import *
from tasks.base.page import page_mimir, page_mimi_observation

class Mimir(AetherGazerHelper):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.connect_device()

    def mimi_observation(self):
        """
        弥弥观测站
        """
        self.ui_goto(page_mimi_observation)
        logger.info("弥弥观测站界面")
        loop_timer = Timer(0, 10).start()

        redispatched = False
        while True:
            if redispatched:
                logger.info("再次派遣完成")
                break

            if loop_timer.reached():
                logger.error("弥弥观测站超出循环次数")
                raise LoopError("弥弥观测站超出循环次数")

            # TODO: 周期奖励添加  
            if self.find_click(MIMI_OBSERVATION_DISPATCH, MIMI_OBSERVATION_DISPATCH, local_search=True):
                redispatched = True
                logger.info("弥弥观测站派遣")
                break

            if self.exists(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK, local_search=True):
                
                while(self.exists(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK, local_search=True)):
                    self.touch(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK, blind=True)
                logger.info("弥弥观测站探索完成")
                continue

            if self.find_click(MIMI_OBSERVATION_CLAIM_ALL, MIMI_OBSERVATION_CLAIM_ALL, local_search=True):
                logger.info("弥弥观测站一键领取奖励")
                continue
    
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
        logger.info("弥弥尔界面")
        self.mimi_observation()