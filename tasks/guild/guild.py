
from tasks.base.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, Timer
from tasks.guild.assets.assets_guild import *
from tasks.base.page import page_guild, page_store_supply
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE, BACK_BUTTON


class Guild(AetherGazerHelper):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)

    def claim_matrix_supply(self):
        """
        领取矩阵补给
        """
        loop_timer = Timer(0, 10).start()

        while True:
            if loop_timer.reached():
                logger.critical("矩阵补给领取超出循环次数")
                return False
            
            if self.exists(GUILD_MATRIX_SUPPLY_COMPLETE):
                logger.info("矩阵补给已领取")
                self.touch(BACK_BUTTON, blind=True)
                break
            if self.find_click(GET_ITEM, CLICK_TO_CONTINUE, local_search=True):
                logger.info("确认领取物品")
                break
            # 检测是否存在领取按钮
            if self.exists(GUILD_MATRIX_SUPPLY_CLAIM):
                self.touch(GUILD_MATRIX_SUPPLY_CLAIM)
                logger.info("领取矩阵补给成功")
                continue
            if self.find_click(GUILD_MATRIX_SUPPLY, GUILD_MATRIX_SUPPLY, local_search=True):
                logger.info("领取矩阵补给")
                continue
        return True
                

    def claim_guild_mission(self):
        """
        公会任务
        """

    def test(self):
        """
        测试函数
        """
        logger.info("测试函数")
        self.ui_goto(page_store_supply)


    def run(self):

        self.ui_ensure(page_guild)
        logger.info("公会界面")
        # self.claim_matrix_supply()
        self.test()




