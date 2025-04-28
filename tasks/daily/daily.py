import numpy as np
from enum import Enum
from typing import Dict, Optional, List, Tuple

from zafkiel import logger, Timer
from zafkiel import Ocr
from zafkiel.ocr import OcrResultButton

from tasks.base.page import page_main, page_activity, page_resource
from tasks.daily.assets.assets_daily import *
from tasks.base.assets.assets_share import BACK_BUTTON
from tasks.daily.keywords import KEYWORDS_ACTIVITY_OPTION, KEYWORDS_RESOURCE_STAGE, KEYWORDS_SIGILS_STAGE
from tasks.base.assets.assets_switch import RESOURCE_ITEMS_SWITCH_ON, RESOURCE_SIGILS_SWITCH_ON
from tasks.daily.clicklist import SIGILS_CLICKLIST
from tasks.battle.battle import Battle
from module.Controller import Controller
from module.AetherGazerHelper import AetherGazerHelper
from config import Config


class ColorEnum(Enum):
    """
    color_level = [R, G, B, priority]
    """

    A = [2]  # A级委托
    B = [1]  # B级委托
    S = [3]  # S级委托


class Daily(Battle):

    SIGILD_MODULE_LEVEL_COLORS: List[List] = []

    def __init__(self, config: Config, controller: Controller) -> None:
        super().__init__(config, controller)

        self.check_and_connect_device()

    def claim_stamina(self):
        """
        领取早上和下午的体力
        to claim free stamina at AM and PM
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

    def use_stamina_on_sigils_module(self):
        """
        联合特勤关卡
        use stamina on sigils page
        """
        # self.ui_ensure(page_resource, state=RESOURCE_SIGILS_SWITCH_ON)
        # logger.info(f"known rows: {SIGILS_CLICKLIST.known_rows}")
        SIGILS_CLICKLIST.select_row(row=KEYWORDS_SIGILS_STAGE.SigilModule, main=self, insight=True, skip_first_screenshot=False)

        self._sigils_module_strategy()
        self.select_stage_sweep_count()

    def _sigils_module_strategy(self):
        """
        联合特勤扫荡策略

        step 1: check S level,
                Yes -> step 2,
                No -> step 3,
        step 2: use stamina 使用体力,
                end.
        step 3: check free refresh 免费刷新,
                Yes -> step 4,
                No -> step 5,
        step 4: refresh 点击刷新,
                jump to step 1
        step 5: choose max level 最高级别,
                jump to step 2
        """
        loop_timer = Timer(5, 5).start()
        stage_list = [SIGILS_MODULE_STAGE_1, SIGILS_MODULE_STAGE_2, SIGILS_MODULE_STAGE_3]  # 3个位置

        def judge_color_level(stage_list: List[Template]) -> Tuple[ColorEnum, Template]:
            """
            Args:
                stage_list: list of stage templates
                image: screenshot image
            Returns:

            """
            result_level_list: List[Tuple[ColorEnum, Template]] = []
            for stage_button in stage_list:
                for color_level in ColorEnum:
                    if self.image_color_count(stage_button, color_level.value[:3]):
                        result_level_list.append([color_level, stage_button])
            result_level_list.sort(key=lambda x: x[-1], reverse=True)  # sorted by priority, max priority at the first
            return result_level_list[0]

        while True:
            if loop_timer.reached():
                logger.error("Can't find Stage within time limit.")
                return False

            # check S level
            max_level, position_template = judge_color_level(stage_list)
            if max_level == 'S':
                break
                # check free refresh
            if self.exists(SIGILS_MODULE_FREE_REFRESH_CHECK, local_search=True):
                # refresh
                self.touch(SIGILS_MODULE_FREE_REFRESH_CHECK, SIGILS_MODULE_FREE_REFRESH_CLICK, local_search=True)

                loop_timer.reset()
                continue
            else:
                # choose max level's position
                self.touch(position_template, local_search=True)
                break
        return True

    def use_stamina_on_joint_defense_agreement(self):
        """
        使用体力扫荡联防协议
        """
        logger.info("Use stamina on joint defense agreement. 使用体力扫荡联防协议")
        self.ui_goto_joint_defense_agreement()
        self.find_click(JOINT_DEFENSE_CHECK, JOINT_DEFENSE_CHECK, local_search=True, blind=True)
        self.select_stage_sweep_count()

        # TODO: 扫荡完成后返回活动界面领取消耗体力的券,可以将返回的界面定义为新的page, 而不是page_activity

    def ui_goto_joint_defense_agreement(self):
        self.ui_ensure(page_activity)
        search_button = ACTIVITY_SEARCH_BUTTON
        ocr = Ocr(search_button, lang='cn')
        loop_timer = Timer(0, 5).start()

        while True:
            if loop_timer.reached():
                logger.error("Can't find Stage within time limit.")
                return False

            button = self.insight_row(row=KEYWORDS_ACTIVITY_OPTION.JointDefenseAgreement, ocr=ocr)
            if len(button) > 0:
                from zafkiel.utils import random_rectangle_point

                x1, y1, x2, y2 = button[0].area
                pos = random_rectangle_point(center=((x1 + x2) / 2, (y1 + y2) / 2), h=y2 - y1, w=x2 - x1)
                self.touch(pos, blind=True)
                break
            self.swipe(v1=ACTIVITY_SWIPE_START, vector=(0, -0.1), blind1=True, blind2=True)
            self.wait_until_stable(search_button, timer=Timer(0, count=0), timeout=Timer(1.5, count=5))
        self.find_click(ACTIVITY_TO_JOINT_DEFENSE, ACTIVITY_TO_JOINT_DEFENSE, local_search=True, blind=True)
        logger.info("Now Select JointDefenseAgreement.")
        return True

    def insight_row(self, row: Keyword, ocr: Ocr) -> list[OcrResultButton]:
        cur_buttons = ocr.ocr_match_keyword(self.controller.screenshot(), keyword_instance=row, mode=2)
        logger.info(f"cur_buttons: {cur_buttons}")
        for button in cur_buttons:
            logger.info(f"button in cur_buttons: {button}")
        return cur_buttons

    def return_event_mission(self):
        self.ui_ensure(page_main)
        # TODO:

    def run(self):
        """
        运行函数
        """
        from utils.logger_func import task_info

        task_info('Daily')

        # self.claim_stamina()
        # self.use_stamina_on_joint_defense_agreement()
        self.use_stamina_on_sigils_module()


if __name__ == '__main__':
    pass
