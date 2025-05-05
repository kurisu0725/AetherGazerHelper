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
        super().__init__(config, controller)

    def is_in_battle(self) -> bool:
        pass

    def get_remain_stamina(self, skip_screenshot=False) -> int:
        """
        获取当前剩余体力
        """
        remain_stamina, _, _ = Battle.get_ocr_digit_or_digit_counter(
            ocr_class=DigitCounter,
            image=self.controller.image if skip_screenshot else self.controller.screenshot(),
            button=REMAIN_STAMINA,
            name="Remain Stamina",
        )
        return remain_stamina

    def get_stamina_cost(self, skip_screenshot=False):
        """
        调用之前必须在扫荡关卡的界面
        """
        # 确保识别到一次扫荡消耗的体力
        self.find_click(LEFT_DOUBLE_ARROW, LEFT_DOUBLE_ARROW)

        stamina_cost = self.get_ocr_digit_or_digit_counter(
            ocr_class=Digit,
            image=self.controller.image if skip_screenshot else self.controller.screenshot(),
            button=STAMINA_COST,
            name="Stamina Cost",
        )
        return stamina_cost

    def select_stage_sweep_count(self, need_back = True, count: int = 10) -> bool:
        """
        choose count of sweep, while checking if there is enough stamina and input param count exceed remain stamina
        选择扫荡次数, 检查是否有足够的体力和输入的次数是否超过剩余体力
        Args:
            count:
        Returns:
            bool:
        """
        remain_stamina = self.get_remain_stamina()
        stamina_cost = self.get_stamina_cost(skip_screenshot=True)
        accept_count = min(count, int(remain_stamina / stamina_cost))
        logger.info(f"Remain Stamina: {remain_stamina}, Stamina Cost: {stamina_cost}, Accept Count: {accept_count} times.")
        success = True
        if accept_count > 0:
            rest_count = accept_count
            loop_timer = Timer(10).start()
            while rest_count > 0:
                if loop_timer.reached():
                    logger.error("Loop timeout. 扫荡超时")
                    raise LoopError("Loop timeout. 扫荡超时")

                if self.find_click(SWEEP_CONFIRM_CHECK, SWEEP_CONFIRM_CLICK, blind=True):
                    self.confirm_battle_end()  # 扫荡-确定
                    rest_count -= min(Battle.BATTLE_SELECT_COUNT_MAX, rest_count)
                    if rest_count <= 0:
                        break
                    loop_timer.reset()
                    continue

                if rest_count >= Battle.BATTLE_SELECT_COUNT_MAX:
                    if self.find_click(RIGHT_DOUBLE_ARROW, RIGHT_DOUBLE_ARROW, blind=True):
                        self.touch(STAGE_SWEEP)
                        continue
                else:
                    if rest_count <= 6:
                        for i in range(rest_count - 1):
                            self.touch(RIGHT_ARROW, blind=True)
                    else:
                        self.find_click(RIGHT_DOUBLE_ARROW, RIGHT_DOUBLE_ARROW, blind=True)
                        for i in range(Battle.BATTLE_SELECT_COUNT_MAX - rest_count):
                            self.touch(LEFT_ARROW, blind=True)
                    self.touch(STAGE_SWEEP)
                    continue

            logger.info(f"Sweep {accept_count} times complete.")
        else:
            logger.info(f"Not enough stamina to sweep {count} times.")
            success = False
        if need_back:
            self.find_click(BACK_BUTTON)
        return success

    @staticmethod
    def get_ocr_digit_or_digit_counter(ocr_class, image, button, lang='en', name=None) -> int:
        digit_ocr = ocr_class(button=button, lang=lang, name=name)
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
        self.wait(SWEEP_END_CHECK)
        self.touch(SWEEP_END_CLICK)
