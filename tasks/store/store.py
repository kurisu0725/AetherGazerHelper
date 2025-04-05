import datetime
import cv2
import time
import shutil
import psutil
import os

from zafkiel import logger
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from tasks.store.assets.assets_store import *
from tasks.base.page import page_store, page_store_supply

class Store(AetherGazerHelper):

    def __init__(self, config : Dict) -> None:
        super().__init__(config)


    def purchase_free_stamina(self):
        """
        Purchase free stamina from the store.
        购买商店的免费体力
        """
        logger.info('Purchase free stamina from the store.')
        self.ui_ensure(page_store)
        
        # self.ui_goto(page_store_supply)

        

    def run(self):
        from utils.logger_func import task_info
        task_info('Store')

        self.connect_device()
        self.purchase_free_stamina()


