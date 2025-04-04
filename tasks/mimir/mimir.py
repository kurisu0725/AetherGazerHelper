
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, find_click, exists, touch, app_is_running
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
        self.ui_ensure(page_mimi_observation)
        logger.info("弥弥观测站界面")
        while True:
            # TODO: 周期奖励添加  
            if find_click(MIMI_OBSERVATION_DISPATCH, MIMI_OBSERVATION_DISPATCH, local_search=True):
                logger.info("弥弥观测站派遣")
                break

            if find_click(MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK, MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK, local_search=True):
                logger.info("弥弥观测站探索完成")
                continue

            if find_click(MIMI_OBSERVATION_CLAIM_ALL, MIMI_OBSERVATION_CLAIM_ALL, local_search=True):
                logger.info("弥弥观测站一键领取奖励")
                continue


    def run(self):
        """
        运行函数
        """
        from utils.logger_func import task_info
        task_info('Mimir')

        self.ui_ensure(page_mimir)
        logger.info("弥弥尔界面")
        self.mimi_observation()