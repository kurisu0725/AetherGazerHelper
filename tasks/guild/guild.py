
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict
from zafkiel import logger, Timer
from tasks.guild.assets.assets_guild import *
from tasks.base.page import page_guild, page_store_supply
from tasks.base.assets.assets_share import GET_ITEM, CLICK_TO_CONTINUE, BACK_BUTTON
from module.Controller import Controller
from config import Config


class Guild(AetherGazerHelper):
    def __init__(self, config: Config, controller: Controller) -> None:
        super().__init__(config, controller)
    def claim_matrix_supply(self):
        """
        领取矩阵补给
        """
        self.ui_ensure(page_guild)
        loop_timer = Timer(0, 10).start()

        while True:
            if loop_timer.reached():
                logger.error("矩阵补给领取超出循环次数")
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
        logger.info("Trying to claim guild mission. 尝试领取公会任务")
        self.ui_ensure(page_guild)
        loop_timer = Timer(3).start()
        claimed = False
        while True:
            if loop_timer.reached():
                if not claimed:
                    logger.error("Guild mission claim timeout, not found claim button. 公会任务领取超时, 未找到领取按钮")
                break
            
            if self.find_click(GUILD_MISSION_CLAIM_CLICK, GUILD_MISSION_CLAIM_CLICK, local_search=True, blind=True):
                self.find_click(GET_ITEM, CLICK_TO_CONTINUE, local_search=True, blind=True)
                claimed = True
                logger.info("Claim guild mission. 领取公会任务")
                loop_timer.reset()

            if self.find_click(GUILD_TO_GUILD_MISSION, GUILD_TO_GUILD_MISSION, local_search=True, blind=True):
                continue
        logger.info("Back to page_guild. 返回公会界面")
        self.touch(BACK_BUTTON)

    def test(self):
        """
        测试函数
        """
        logger.info("测试函数")
        self.ui_goto(page_store_supply)


    def run(self):

        # self.ui_ensure(page_guild)
        logger.info("公会界面")
        self.claim_matrix_supply()
        # self.test()
        self.claim_guild_mission()





