import numpy as np
import re
from typing import Dict, Final, Union
from module.AetherGazerHelper import AetherGazerHelper
from module.Controller import Controller
from tasks.base.page import page_dorm, page_dorm_nav_kitchen, page_dorm_nav_character
from tasks.base.assets.assets_share import BACK_BUTTON, GET_ITEM, CLICK_TO_CONTINUE
from tasks.dorm.assets.assets_dorm import *
from zafkiel.exception import LoopError
from zafkiel import Timer, logger
from zafkiel.ocr import Digit, Ocr
from zafkiel.utils import crop
from config import Config
from module.ocr import DigitCounter
from module.utils import hough_circle

class Dorm(AetherGazerHelper):

    _TRAIN_BUTTON : list[Template] | None = None
    _TRAIN_BUTTON_CLICK : list[Template] | None = None

    TRAIN_MODIFIER_COST : Final[int] = 20
    MODIFIER_COMBAT_MAX_COUNT : Final[int] = 6

    def __init__(self, config: Config, controller: Controller):
        super().__init__(config, controller)

        # self.check_and_connect_device()
        
    @classmethod
    def get_train_buttons(cls) -> list[Template]:
        if cls._TRAIN_BUTTON is None:
            cls._TRAIN_BUTTON = [
                value for name, value in globals().items() 
                if re.match(r"TRAIN_MODIFIER_ABILITY_\d+(?!_CLICK)", name)
            ]
        return cls._TRAIN_BUTTON

    @classmethod
    def get_train_buttons_click(cls) -> list[Template]:
        if cls._TRAIN_BUTTON_CLICK is None:
            cls._TRAIN_BUTTON_CLICK = [
                value for name, value in globals().items()
                if re.match(r"TRAIN_MODIFIER_ABILITY_\d+_CLICK", name)
            ]
        return cls._TRAIN_BUTTON_CLICK

    def claim_kitchen(self):
        """
        Claim kitchen resources.
        """
        self.ui_ensure(page_dorm_nav_kitchen)

        loop_timer = Timer(0, 10).start()
        while True:
            if loop_timer.reached():
                raise LoopError("Claim kitchen resources timed out.")
            
            # TODO: 还存在一个 "确定"情况，领取上次派遣

            if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK, blind=True):
                logger.info("Assigned kitchen tasks.")
                break
            
            if self.find_click(DORM_NAV_KITCHEN_CURRENCY_CLAIM, DORM_NAV_KITCHEN_CURRENCY_CLAIM, blind=True):
                logger.info("Claimed kitchen resources.")
                continue

            if self.find_click(DORM_NAV_KITCHEN_TASK_ASSIGN, DORM_NAV_KITCHEN_TASK_ASSIGN, blind=True):
                logger.info("Exit claim_kitchen tasks.")
                continue

        self.touch(BACK_BUTTON, blind=True)

    def train_modifiers(self):
        """
        Train modifiers in the dormitory.
        训练修正者
        """
        self.ui_ensure(page_dorm_nav_character)
        # 霍夫圆检测 + 图像匹配
        
        # enter train page 
        self.find_click(TO_TRAIN)

        # swipe and train modifier
        self._train_modifiers()
        self.find_click(BACK_BUTTON, blind=True)

    def modifier_combat(self, num_of_combat : int = 1):
        enable_combat : bool = self.config.data['Menu']['Dorm']['Combat']['enable_combat']
        weekly_combat_count : int = self.config.data['Menu']['Dorm']['Combat']['weekly_combat_count']
        last_combat_time : str = self.config.data['Menu']['Dorm']['Combat']['last_combat_time']

        if enable_combat is False:
            logger.info("Modifier combat is disabled. Skip this task.")
            return

        if weekly_combat_count == Dorm.MODIFIER_COMBAT_MAX_COUNT:
            logger.info("The number of  combats recorded has reached the limit.")
            return 

        if len(last_combat_time) == 0 or last_combat_time is None:
            weekly_combat_count = 0
            self.config.update('Menu.Dorm.Group.last_combat_time', weekly_combat_count)

        # TODO: 和周一的时间比较

        self.ui_ensure(page_dorm_nav_character)
        loop_timer = Timer(0, 10).start()

        while True:
            if loop_timer.reached():
                logger.critical("Modifier combat end for unknown reason. ")
                break
            
            if self.exists(MODIFIER_COMBATTING_CHECK):
                self.sleep(5)
                loop_timer.reset()
                continue
            
            if self.exist(MODIFIER_COMBAT_END_CHECK):
                num_of_combat -= 1
                self.config.update('Menu.Dorm.Group.last_combat_time', weekly_combat_count)
                if num_of_combat == 0:
                    self.touch(MODIFIER_COMBAT_END_CLICK)
                    logger.info("Modifier combat end.")
                    break
                else:
                    self.touch(MODIFIER_COMBAT_AGAIN)
                    logger.info(f"Modifier combat again. Rest {num_of_combat} times.")
                continue


            if self.find_click(MODIFIER_COMBAT_SELECT_STRANGER, MODIFIER_COMBAT_SELECT_STRANGER, blind=True, times=2):
                self.find_click(MODIFIER_COMBAT_SELECT_TO_CHALLENGE, MODIFIER_COMBAT_SELECT_TO_CHALLENGE, blind=True, times=2)
                continue

            if self.find_click(MODIFIER_COMBAT_CLICK, MODIFIER_COMBAT_CLICK, blind=True):
                continue

            if self.find_click(TO_MODIFIER_COMBAT, TO_MODIFIER_COMBAT, blind=True):
                continue

        self.touch(BACK_BUTTON)
                

    
    def claim_train_mission(self):
        """
        领取训练任务
        """
        self.ui_ensure(page_dorm_nav_character)

        self.touch(TO_TRAIN_MISSION)

        if self.find_click(TRAIN_MISSION_CLAIM_CHECK, TRAIN_MISSION_CLAIM_CLICK, ocr_mode=2):
            self.find_click(GET_ITEM, CLICK_TO_CONTINUE, blind=True)
            logger.info("Dorm train missions claim.")
        else:
            logger.info("No dorm train mission to claim.")
        self.touch(BACK_BUTTON, blind=True)

    def _train_modifiers(self):
        
        search_button = TRAIN_SEARCH_BUTTON
        logger.info(f"search button filepath: {search_button.filepath}")
        loop_timer = Timer(0, 10).start()

        self.controller.screenshot()

        ocr_train_count = DigitCounter(button=OCR_TRAIN_COUNT, name='modifier_count')
        cur_count, _, _ = ocr_train_count.ocr_single_line(self.controller.image)
        search_image = crop(self.controller.image, search_button.area)
        circles = hough_circle(search_image, sort_func=lambda circle: circle[1])
        circle_idx = 0
        cur_rect_image_list = self.get_hough_circle_crop_image(search_image, circles)
        last_rect_image = cur_rect_image_list[-1]
    
        
        upper_left = tuple( int(i) for i in search_button.area)[:2]

        while True:
            if loop_timer.reached():
                logger.critical("Train modifier ended. Maybe all of modifiers' stats are full.")
                break
            
            if cur_count == 0:
                logger.info("Train modifier success, rest count equals 0.")
                break
            
            logger.info(f"cur_count: {cur_count}, hough circles: {len(circles)}, circle_idx: {circle_idx}, ")

            if circle_idx >= len(circles):
                start_circle = tuple( int(i) for i in circles[1][:2] )
                end_circle = tuple( int(i) for i in circles[0][:2] )
                self.swipe([sum(values) for values in zip(start_circle, upper_left)], [sum(values) for values in zip(end_circle, upper_left)], blind1=True, blind2=True)

                self.wait_until_stable(search_button, timer=Timer(
                    0.3, count=1), timeout=Timer(1.5, count=5))
                self.controller.screenshot()
                search_image = crop(self.controller.image, search_button.area)
                circles = hough_circle(search_image, sort_func=lambda circle: circle[1])
                cur_rect_image_list = self.get_hough_circle_crop_image(search_image, circles)
                match_idx = self.get_last_rect_image_idx(last_rect_image, cur_rect_image_list)
                logger.info(f"match idx: {match_idx}")
                if match_idx == len(circles) - 1:
                    logger.info("Already in the bottom of list.")
                    break
                circle_idx = match_idx + 1
                last_rect_image = cur_rect_image_list[-1]
                loop_timer.reset()

            #点击circle_idx 对应的修正者
            pos = tuple(sum(values) for values in zip(upper_left, tuple(int(i) for i in circles[circle_idx][:2]) ))
            self.touch( v = pos )
            # 开始训练
            cur_count = self.click_train_button(count=cur_count)
            circle_idx += 1
                
    def get_hough_circle_crop_image(self, search_button : Union[Template, np.ndarray], circles):
        """
        得到霍夫圆检测后，以圆心为中心crop出的矩形图像 作为匹配
        """
        search_image = None
        if isinstance(search_button, Template):
            search_image = crop(self.controller.image, search_button.area)
        elif isinstance(search_button, np.ndarray):
            search_image = search_button
        else:
            raise TypeError("search_button must be Template or np.ndarray")
        rect_image_list = []
        rect_height, rect_width = 50, 50
        for x, y, r in circles:
            rect_image_list.append(search_image[int(y - rect_height / 2) : int(y + rect_height / 2), int(x - rect_width / 2) : int(x + rect_width / 2), :])
        return rect_image_list

    def get_last_rect_image_idx(self, last_rect_image, cur_rect_image_list):
        from module.utils import match_template
        for idx in range(len(cur_rect_image_list)):
            rect_image = cur_rect_image_list[idx]
            if match_template(rect_image, last_rect_image):
                return idx
        return -1


    def click_train_button(self, count : int) -> bool:
        """
        存在点击后无反馈的情况(派遣)
        """
        ocr_modifier_stamina : DigitCounter = DigitCounter(button=OCR_TRAIN_MODIFIER_STAMINA, name='modifier_stamina')
        ocr_full_stats_list : list[Ocr] = []
        modifier_stamina : int = 0
        train_button = Dorm.get_train_buttons()
        train_button_click = Dorm.get_train_buttons_click()
        for i in range(len(train_button)):
            ocr_full_stats_list.append(Ocr(button=train_button[i], name=f'modifier_full_stats_{i + 1}'))

        for i in range(len(train_button)):
            button = train_button[i]
            button_click = train_button_click[i]
            loop_timer = Timer(5).start()
            is_dispatched = False
            while True:
                if count <= 0:
                    return count

                if loop_timer.reached():
                    logger.info("Train modifier failed. Maybe this modifier's all stats are full.")
                    return count
                # 某些情况下的ocr stamina 识别失败 120 识别为 -> 0? case '120 /120' 会导致失效,已修复。见module/ocr.py
                modifier_stamina, _, _ = ocr_modifier_stamina.ocr_single_line(self.controller.screenshot())
                logger.info(f"Ocr modifier stamina: {modifier_stamina}")
                if modifier_stamina < Dorm.TRAIN_MODIFIER_COST:
                    break
                
                is_full_stats = ocr_full_stats_list[i].ocr_match_keyword(self.controller.image, Keyword(u'已满'))
                if is_full_stats:
                    logger.info(f"Modifier's number {i + 1} stat is full.")
                    break

                if self.find_click(button, button_click, times = 2, blind=True):
                    cur_modifier_stamina, _, _ = ocr_modifier_stamina.ocr_single_line(self.controller.screenshot())
                    if modifier_stamina == cur_modifier_stamina:
                        is_dispatched = True
                        logger.info("Train modifier failed. This modifier maybe in kitchen dispatch.")
                        break
                    modifier_stamina = cur_modifier_stamina
                    count -= 1
                    loop_timer.reset()
                    continue
            if is_dispatched:
                break
        return count

    def test_func(self):
        ocr_modifier_stamina : DigitCounter = DigitCounter(button=OCR_TRAIN_MODIFIER_STAMINA, name='modifier_stamina')
        modifier_stamina, zero, total_stamina = ocr_modifier_stamina.ocr_single_line(self.controller.screenshot())
        logger.info(f"modifier_stamina: {modifier_stamina}, zero: {zero}, total_stamina: {total_stamina}")

    def run(self):
        """
        Main function to run the dormitory task.
        """
        # self.ui_ensure(page_dorm)

        self.claim_kitchen()

        # self.train_modifiers()
        
        # self.modifier_combat()

        # self.claim_train_mission()