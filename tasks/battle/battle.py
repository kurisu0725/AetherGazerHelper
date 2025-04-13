from zafkiel.ui import UI
from typing import Dict, Final
from zafkiel import Template, logger, Timer
from zafkiel.exception import LoopError
from zafkiel.ocr import Ocr, DigitCounter, Digit
from utils.logger_func import task_info
from module.Controller import Controller
from module.AetherGazerHelper import AetherGazerHelper
from tasks.battle.assets.assets_battle import *
from tasks.base.assets.assets_share import *
from config import Config

class Battle(AetherGazerHelper):

    BATTLE_SELECT_COUNT_MAX: Final[int] = 10

    def __init__(self, config: Config, controller: Controller):
        super().__init__(config, controller)  # 单一路径初始化

    def is_in_battle(self) -> bool:
        pass

    def select_stage_sweep_count(self, count: int = 1):
        """
        choose count of sweep, while checking if there is enough stamina and input param count exceed remain stamina
        选择扫荡次数, 检查是否有足够的体力和输入的次数是否超过剩余体力
        Args:
            count:  
        Returns:
        """
        remain_stamina, _, _ = self.get_ocr_digit_or_digit_counter(ocr_class=DigitCounter, image=self.controller.screenshot(), button=REMAIN_STAMINA, name= "Remain Stamina")
        stamina_cost = self.get_ocr_digit_or_digit_counter(ocr_class=Digit, image=self.controller.screenshot(), button=STAMINA_COST, name= "Stamina Cost")

        accept_count = min(count, remain_stamina / stamina_cost)
        logger.info(f"Remain Stamina: {remain_stamina}, Stamina Cost: {stamina_cost}, Accept Count: {accept_count} times.")
        if accept_count > 0:
            rest_count = accept_count
            loop_timer = Timer(10).start()
            while rest_count > 0:
                if loop_timer.reached():
                    raise LoopError("Loop timeout")
                
                if self.find_click(SWEEP_CONFIRM_CHECK, SWEEP_CONFIRM_CLICK, blind=True):
                    self.confirm_battle_end()       #扫荡-确定
                    rest_count -= min(Battle.BATTLE_SELECT_COUNT_MAX, rest_count)
                    loop_timer.reset()

                if self.find_click(RIGHT_DOUBLE_ARROW, RIGHT_DOUBLE_ARROW, blind=True):
                    self.touch(STAGE_SWEEP)
                    continue
            logger.info(f"Sweep {accept_count} times complete.")
        else:
            logger.info(f"Not enough stamina to sweep {count} times.")
        self.find_click(BACK_TO_MAIN)

    @staticmethod
    def get_ocr_digit_or_digit_counter(ocr_class, image, button, lang = 'en', name = None) -> int:
        digit_ocr = ocr_class(button=button , lang=lang, name=name)
        if isinstance(digit_ocr, Digit) or isinstance(digit_ocr, DigitCounter):
            return digit_ocr.ocr_single_line(image)
        else:
            logger.error("ocr_class is not Digit or DigitCounter")
            raise TypeError("ocr_class is not Digit or DigitCounter")

    def check_sweep_button_available(self) -> bool:
        is_exist = self.exists(STAGE_SWEEP)
        if is_exist == False:
            logger.error("Sweep button is not available, please combat at this stage once. 扫荡按钮未解锁，请在本关卡战斗一次。")
        return is_exist
    def confirm_battle_end(self):
        return self.find_click(SWEEP_END_CHECK, SWEEP_END_CLICK, blind=True)



        