
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict, Optional
from zafkiel import logger, Timer
from tasks.base.page import page_main, page_activity, page_store_supply
from tasks.daily.assets.assets_daily import *
from tasks.base.assets.assets_share import BACK_BUTTON
from module.Controller import Controller
from zafkiel import Ocr
from zafkiel.ocr import OcrResultButton
from tasks.daily.keywords.classes import ActivityOption
from tasks.daily.keywords import KEYWORDS_ACTIVITY_OPTION

class Daily(AetherGazerHelper):
    def __init__(self, config: Dict, controller: Controller) -> None:
        super().__init__(config, controller)
        

    def claim_stamina(self):
        """
        领取早上和下午的体力
        to claim free stamina in AM and PM
        """
        self.ui_ensure(page_main)
        if self.exists(MAIN_TO_STAMINA, timeout=5, local_search=True):
            logger.info("前往领取体力")
            self.touch(MAIN_TO_STAMINA, local_search=True)
            if self.find_click(DAILY_STAMINA_CLAIM_AM, DAILY_STAMINA_CLAIM_AM, times=2, local_search=True):
                logger.info("领取早上体力")
            else:
                logger.warning("没有早上体力,或者已经领取")
            if self.find_click(DAILY_STAMINA_CLAIM_PM, DAILY_STAMINA_CLAIM_PM, times=2, local_search=True):
                logger.info("领取晚上体力")
            else:
                logger.info("没有晚上体力,或者已经领取")
            # 返回主界面, 这里使用BACK_BUTTON只是偷懒, 点击任意其他地方也可以
            self.touch(BACK_BUTTON, blind=True)
        else:
            logger.info("匹配失败")

    def use_stamina(self):
        """
        TODO: 使用体力扫荡联防协议，或日常资源关卡
        """
        from tasks.base.assets.assets_page import MAIN_CHECK
        # self.find_click(MAIN_CHECK, MAIN_CHECK, local_search=True)
        # self.ui_ensure(page_main)
        logger.info("使用体力扫荡联防协议，或日常资源关卡")
        self.goto_joint_defense_agreement()


    def goto_joint_defense_agreement(self):
        from airtest.core.api import ST
        self.ui_ensure(page_activity)
        ocr = Ocr(ACTIVITY_SEARCH_BUTTON, lang='cn')
        loop_timer = Timer(0, 5).start()
        while True:
            if loop_timer.reached():
                logger.error("Can't find Stage within time limit.")
                return False
            
            button = self.insight_row(row=KEYWORDS_ACTIVITY_OPTION.JointDefenseAgreement, keyword_cls=ActivityOption,ocr=ocr)[0]
            logger.info("")
            if button is not None:
                self.touch(button.area, blind=True)
                logger.info("Find Stage.")
                break
            self.swipe(v1=ACTIVITY_SWIPE_START, vector=(0, -0.15), blind1=True, blind2=True)
            self.sleep(ST.OPDELAY)
        return True

    def insight_row(self, row: Keyword, keyword_cls: Keyword, ocr: Ocr) -> list[OcrResultButton]:

        cur_buttons = ocr.ocr_match_keyword(self.controller.screenshot(), keyword_instance=row, mode=2)
        logger.info(f"cur_buttons: {cur_buttons}")
        for button in cur_buttons:
            logger.info(f"button: {button}")
        return button

    def run(self):
        """
        运行函数
        """
        from utils.logger_func import task_info
        task_info('Daily')

        # self.claim_stamina()
        self.use_stamina()

if __name__ == '__main__':
    pass