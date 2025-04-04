
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, find_click, exists, touch, app_is_running
from tasks.guild.assets.assets_guild import *
from tasks.base.page import page_guild
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE


class Guild(AetherGazerHelper):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)
        self.connect_device()

    def claim_matrix_supply(self):
        """
        领取矩阵补给
        """
        while True:
            if exists(GUILD_MATRIX_SUPPLY_COMPLETE):
                logger.info("矩阵补给已领取")
                break
            if find_click(GET_ITEM, CLICK_TO_CONTINUE, local_search=True):
                logger.info("确认领取物品")
                break
            # 检测是否存在领取按钮
            if exists(GUILD_MATRIX_SUPPLY_CLAIM):
                touch(GUILD_MATRIX_SUPPLY_CLAIM)
                logger.info("领取矩阵补给成功")
                continue
            if find_click(GUILD_MATRIX_SUPPLY, GUILD_MATRIX_SUPPLY, local_search=True):
                logger.info("领取矩阵补给")
                continue
                

    def claim_guild_mission(self):
        """
        公会任务
        """

    def run(self):

        self.ui_ensure(page_guild)
        logger.info("公会界面")
        self.claim_matrix_supply()
        pass



