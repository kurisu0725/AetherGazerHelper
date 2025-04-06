import datetime
import cv2
import time
import shutil
import psutil
import os

from zafkiel import logger, Timer
from zafkiel.exception import LoopError
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from tasks.store.assets.assets_store import *
from tasks.base.assets.assets_share import *
from tasks.base.page import page_store, page_store_supply

class Store(AetherGazerHelper):

    def __init__(self, config : Dict) -> None:
        super().__init__(config)


    def purchase_free_stamina(self):
        """
        Purchase free stamina from the store.
        购买商店的免费体力
        """
        logger.info('购买商店的免费体力.')
        self.ui_ensure(page_store_supply)
        loop_timer = Timer(0, 10).start()


        while True:
            if loop_timer.reached():
                logger.error("商店购买免费体力超出循环次数, 可能已经领取过免费体力.")
                return False
            
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, local_search=True, blind=True):
                logger.info("获得免费体力.")
                break
            
            if self.find_click(STORE_SUPPLY_PURCHASE_CHECK, STORE_SUPPLY_PURCHASE_CLICK, local_search=True, blind=True):
                logger.info("点击确定购买.")
                continue

            if self.exists(STORE_SUPPLY_FREE_STAMINA_CHECK, local_search=True):
                self.find_click(STORE_SUPPLY_FREE_STAMINA_CLICK, local_search=True, blind=True)
                logger.info("点击免费体力.")
                continue

            if self.find_click(STORE_SUPPLY_DAILY_SUPPLY_CLICK, local_search=True, blind=True):
                logger.info("切换到日常补给选项.")
                continue

        logger.info("每日免费体力完成.")
        return True

    def run(self):
        from utils.logger_func import task_info
        task_info('Store')
        self.purchase_free_stamina()


