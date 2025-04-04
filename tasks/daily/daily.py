
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, find_click, exists, touch
from tasks.base.page import page_main
from tasks.daily.assets.assets_daily import *
from tasks.base.assets.assets_share import BACK_BUTTON

class Daily(AetherGazerHelper):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.connect_device()

    def claim_stamina(self):
        """
        领取体力
        """
        self.ui_ensure(page_main)
        if exists(MAIN_TO_STAMINA, timeout=5, local_search=False):
            logger.info("前往领取体力")
            touch(MAIN_TO_STAMINA, local_search=True)
            if find_click(DAILY_STAMINA_CLAIM_AM, DAILY_STAMINA_CLAIM_AM, times=2, local_search=True):
                logger.info("领取早上体力")
            else:
                logger.info("没有早上体力,或者已经领取")
            if find_click(DAILY_STAMINA_CLAIM_PM, DAILY_STAMINA_CLAIM_PM, times=2, local_search=True):
                logger.info("领取晚上体力")
            else:
                logger.info("没有晚上体力,或者已经领取")
            # 返回主界面, 这里使用BACK_BUTTON只是偷懒, 点击任意其他地方也可以
            touch(BACK_BUTTON, blind=True)
        else:
            logger.info("匹配失败")

    def run(self):
        """
        运行函数
        """
        from utils.logger_func import task_info
        task_info('Daily')
        logger.info("日常任务")
        self.claim_stamina()