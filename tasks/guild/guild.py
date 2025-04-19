
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

        self.check_and_connect_device()
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
        
        self.touch(BACK_BUTTON, blind=True)
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

    def purchase_guild_store_item(self):
        """
        购买公会商店物品
        """
        from module.utils import get_format_time
        enable_purchase_guild_store = self.config.data['Basic']['Guild']['Guild_Store']['enable_purchase_guild_store']
        last_purchase_guild_store_time = self.config.data['Basic']['Guild']['Guild_Store']['last_purchase_guild_store_time']

        if enable_purchase_guild_store == False:
            logger.info("Disenable purchase guild store item, skip. 未开启购买公会商店物品功能, 跳过.")
            return
        
        if len(last_purchase_guild_store_time) == 0 or last_purchase_guild_store_time is None:
            logger.info("The time of purchasing guild store item is not recorded, assume it is not purchased. 未记录购买公会商店物品时间, 判断为未购买.")
        elif last_purchase_guild_store_time >= get_format_time(is_now=False):
            logger.info("Guild item has been have purchased this week, skip. 本周已经购买了公会商店物品, 跳过.")
            return
        
        # TODO: 具体操作的代码
        self.ui_ensure(page_guild)
        self.find_click(GUILD_TO_GUILD_STORE)

        stat1 = self.purchase_item(GUILD_STORE_SIGIL_CORE, local_search=False)

        stat2 = self.purchase_item(GUILD_STORE_SIGIL_MODULE_T3, local_search=False)

        if stat1 and stat2:
            logger.info("Purchase guild store item success. 购买公会商店物品成功")
            last_purchase_guild_store_time = get_format_time()
            logger.info(f"Record last_purchase_guild_store_time : {last_purchase_guild_store_time}")
            self.config.update(menu = 'Basic', task = 'Guild', group = 'Guild_Store', item = 'last_purchase_guild_store_time', value = last_purchase_guild_store_time)
        else:
            logger.error("Purchase guild store item failed. 购买公会商店物品失败")

       
    def purchase_item(self, item: Template, local_search: bool = True):
        loop_timer = Timer(0, 10).start()
        while True:
            if loop_timer.reached():
                logger.error("Purchase item timeout, not found purchase button. 购买物品超时, 未找到购买按钮")
                return False
            
            if self.exists(GUILD_STORE_PURCHASE_CLICK):
                from zafkiel.ocr import Digit
                from module.ocr import DigitCounter
                ocr_number_limit = DigitCounter(button=GUILD_STORE_PURCHASE_LIMIT_NUMBER, name="GUILD_STORE_PURCHASE_LIMIT_NUMBER")
                ocr_number_purchase = Digit(button=GUILD_STORE_PURCHASE_NUMBER, name="GUILD_STORE_PURCHASE_NUMBER")
                rest_number, _, _ = ocr_number_limit.ocr_single_line(self.controller.screenshot())
                cur_number = ocr_number_purchase.ocr_single_line(self.controller.image)
                if cur_number > rest_number:
                    self.touch(BACK_BUTTON)
                    logger.info("No enough item.剩余物品不足")
                else:
                    timeout = Timer(0, 3).start()
                    while cur_number < rest_number:
                        if timeout.reached():
                            logger.error("Purchase item timeout. 购买物品超时, 资源不足以购买全部数量")
                            break
                        self.touch(GUILD_STORE_PURCHASE_PLUS, blind=True)
                        last_number = cur_number
                        cur_number = ocr_number_purchase.ocr_single_line(self.controller.screenshot())
                        if last_number != cur_number:
                            timeout.reset()
                        logger.info(f"Cur number: {cur_number}, Rest number: {rest_number}")
                    self.touch(GUILD_STORE_PURCHASE_CLICK)
                    logger.info("Click purchase button. 点击购买按钮")
                break
                
            if self.find_click(item, local_search=local_search):
                logger.info("Find item. 找到物品")
                continue
        return True

    def run(self):

        # self.ui_ensure(page_guild)
        self.claim_matrix_supply()
        # self.claim_guild_mission()
        # self.purchase_guild_store_item()





