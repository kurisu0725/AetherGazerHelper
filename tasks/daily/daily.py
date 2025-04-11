
from module.AetherGazerHelper import AetherGazerHelper
from typing import Dict, Optional
from zafkiel import logger, Timer
from tasks.base.page import page_main, page_activity, page_resource
from tasks.daily.assets.assets_daily import *
from tasks.base.assets.assets_share import BACK_BUTTON
from module.Controller import Controller
from zafkiel import Ocr
from zafkiel.ocr import OcrResultButton
from tasks.daily.keywords.classes import ActivityOption
from tasks.daily.keywords import KEYWORDS_ACTIVITY_OPTION
from tasks.base.assets.assets_switch import RESOURCE_ITEMS_SWITCH_ON
from tasks.daily.clicklist import ITEMCLICKLIST
from tasks.battle.battle import Battle

class Daily(Battle):
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

    def use_stamina_on_daily_resource(self):
        """
        暂时在资源界面使用
        use stamina on resource page
        """
        self.ui_ensure(page_resource, state=RESOURCE_ITEMS_SWITCH_ON)
        

    def use_stamina_on_joint_defense_agreement(self):
        """
        TODO: 使用体力扫荡联防协议
        """
        logger.info("使用体力扫荡联防协议")
        self.ui_goto_joint_defense_agreement()
        self.select_stage_sweep_count(count=1)


        # TODO: 扫荡完成后返回活动界面领取消耗体力的券


    def ui_goto_joint_defense_agreement(self):
        from airtest.core.api import ST
        self.ui_ensure(page_activity)
        search_button = ACTIVITY_SEARCH_BUTTON
        ocr = Ocr(search_button, lang='cn')
        loop_timer = Timer(0, 5).start()
        
        while True:
            if loop_timer.reached():
                logger.error("Can't find Stage within time limit.")
                return False
            
            button = self.insight_row(row=KEYWORDS_ACTIVITY_OPTION.JointDefenseAgreement,ocr=ocr)
            if len(button) > 0:
                from zafkiel.utils import random_rectangle_point
                button = button[0]
                x1, y1, x2, y2 = button.area
                pos = random_rectangle_point(center=( (x1 + x2) / 2, (y1 + y2) / 2), h=y2 - y1, w=x2 - x1)
                self.touch(pos, blind=True)
                break
            self.swipe(v1=ACTIVITY_SWIPE_START, vector=(0, -0.1), blind1=True, blind2=True)
            self.wait_until_stable(search_button, timer=Timer(
                0, count=0), timeout=Timer(1.5, count=5))
        
        logger.info("Now Select JointDefenseAgreement.")
        return True

    def insight_row(self, row: Keyword, ocr: Ocr) -> list[OcrResultButton]:
        cur_buttons = ocr.ocr_match_keyword(self.controller.screenshot(), keyword_instance=row, mode=2)
        logger.info(f"cur_buttons: {cur_buttons}")
        for button in cur_buttons:
            logger.info(f"button in cur_buttons: {button}")
        return cur_buttons

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