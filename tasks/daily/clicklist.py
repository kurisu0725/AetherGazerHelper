import numpy as np
from typing import Optional
from zafkiel import Template, logger, Timer
from zafkiel.ocr import OcrResultButton, Keyword, Ocr
from module.AetherGazerHelper import AetherGazerHelper
from tasks.daily.assets.assets_daily import RESOURCE_NEXT_BUTTON, RESOURCE_SEARCH_BUTTON, RESOURCE_PREV_BUTTON
from .keywords.classes import ResourceStage
from zafkiel.utils import random_rectangle_point

class ClickList:
    """
    和可拖拽的list不同，相对拖拽的惯性画面要稳定
    应用在日常资源的关卡中，都是可以通过点击的方式切换到下一个列表项，位置也会变换
    """
    def __init__(
        self,
        name, 
        keyword_class,
        ocr_class,
        search_button: Template,
        next_button: Template,
        prev_button: Template,
        switch_name: Optional[str] = None,
    ) -> None:
        """
        Args:
            search_button: 固定位置的模板, 当前选中的区域 
            next_button: 下一个索引的固定位置
            prev_button: 上一个索引的固定位置
        """
        self.name = name
        self.keyword_class = keyword_class
        self.ocr_class = ocr_class
        self.known_rows = list(keyword_class.instances.values())
        logger.info(f'clicklist.known_rows: {self.known_rows} initialized')

        self.search_button = search_button
        self.next_button = next_button
        self.prev_button = prev_button
        self.switch_name = switch_name

        self.row_min = 1
        self.row_max = len(self.known_rows)
        self.cur_min = 1
        self.cur_max = 1
        self.cur_buttons: list[OcrResultButton] = []

    def __str__(self):
        return f'DraggableList({self.name})'

    __repr__ = __str__

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(self.name)

    def keyword2index(self, row: Keyword) -> int:
        try:
            return self.known_rows.index(row) + 1
        except ValueError:
            # logger.warning(f'Row "{row}" does not belong to {self}')
            return 0

    # def is_row_selected(self, button: OcrResultButton, main: AetherGazerHelper) -> bool:
    #     # Having gold letters
    #     if main.image_color_count(button, color=self.active_color, threshold=221, count=50):
    #         return True

    #     return False

    def keyword2button(self, row: Keyword, show_warning=True) -> Optional[OcrResultButton]:
        for button in self.cur_buttons:
            if button == row:
                return button

        if show_warning:
            logger.warning(f'Keyword {row} is not in current rows of {self}')
            logger.warning(f'Current rows: {self.cur_buttons}')
        return None

    def load_rows(self, main: AetherGazerHelper):
        """
        Parse current rows to get list position.
        """
        self.cur_buttons = self.ocr_class(self.search_button) \
            .matched_ocr(main.controller.image, self.keyword_class)
        # Get indexes
        indexes = [self.keyword2index(row.matched_keyword)
                   for row in self.cur_buttons]
        indexes = [index for index in indexes if index]
        
        if not indexes:
            logger.warning(f'No valid rows loaded into {self}')
            return

        self.cur_min = min(indexes)
        self.cur_max = max(indexes)
        logger.info(self.name, f'{self.cur_min} - {self.cur_max}')

    def insight_row(self, row: Keyword, main: AetherGazerHelper, skip_first_screenshot=True) -> bool:
        """
        Args:
            row:
            main:
            skip_first_screenshot:
        Returns:
            bool: True if row is detected.
        """
        dest_row_index = self.keyword2index(row)
        if not dest_row_index:
            logger.warning(f'Insight row {row} but index unknown')
            return False
        
        logger.info(f'Insight row: {row}, index={dest_row_index}')
        last_buttons: set[OcrResultButton] = None
        bottom_check = Timer(3, count=5).start()
        while True:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                main.controller.screenshot()

            self.load_rows(main=main)
            logger.info(f'Current rows: {self.cur_buttons}')
            # End
            if self.cur_buttons and self.cur_min <= dest_row_index <= self.cur_max:
                break

            cur_row_index = self.keyword2index(self.cur_buttons[0].matched_keyword)

            if cur_row_index < dest_row_index:
                main.controller.touch(self.next_button, blind=True)
            elif cur_row_index > dest_row_index:
                main.controller.touch(self.prev_button, blind=True)
            main.wait_until_stable(self.search_button)

            if self.cur_buttons and last_buttons == set(self.cur_buttons):
                if bottom_check.reached():
                    logger.warning(f'No more rows in {self}')
                    return False
            else:
                bottom_check.reset()
            last_buttons = set(self.cur_buttons)
        return True



    def select_row(self, row: Keyword, main: AetherGazerHelper, insight=True, skip_first_screenshot=True):
        if insight:
            result = self.insight_row(
                row, main=main, skip_first_screenshot=skip_first_screenshot)
            if not result:
                return False
        logger.info(f'Select row: {row}')
        skip_first_screenshot = True
        
        skip_first_load_rows = True
        load_rows_interval = Timer(1)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                main.controller.screenshot()

            if skip_first_load_rows:
                skip_first_load_rows = False
                load_rows_interval.reset()
            else:
                if load_rows_interval.reached():
                    self.load_rows(main=main)
                    load_rows_interval.reset()

            button = self.keyword2button(row)
            if not button:
                return False
            else:
                x1, y1, x2, y2 = button.area
                pos = random_rectangle_point(center=( (x1 + x2) / 2, (y1 + y2) / 2), h=y2 - y1, w=x2 - x1)
                main.controller.touch(pos, times=2, blind=True)
                return True


ITEMCLICKLIST = ClickList(
    name="ItemClickList",
    keyword_class=ResourceStage,
    ocr_class=Ocr,
    search_button=RESOURCE_SEARCH_BUTTON,
    next_button=RESOURCE_NEXT_BUTTON,
    prev_button=RESOURCE_PREV_BUTTON,
)

