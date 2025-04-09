import numpy as np

from typing import Optional
from zafkiel import Template
from zafkiel.ocr.ocr import OcrResultButton
from zafkiel.ocr import Keyword
from zafkiel import logger, Timer
from module.AetherGazerHelper import AetherGazerHelper

"""
modified from SRC: 
"""

class DraggableList:

    def __init__(
        self,
        name, 
        keyword_class,
        ocr_class,
        search_button: Template,
        check_row_order: bool = True,
        active_color: tuple[int, int, int] = (190, 175, 124),
        drag_direction: str = "down",
        is_list_changeable: bool = False,
    ):
        """
        Args:
            name:
            keyword_class: Keyword
            search_button:
            drag_direction: Default drag direction to higher index
            is_list_changeable: If the list is changeable, self.known_rows 
        """
        self.name = name
        self.keyword_class = keyword_class
        self.ocr_class = ocr_class
        if isinstance(keyword_class, list):
            keyword_class = keyword_class[0]
        self.known_rows = list(keyword_class.instances.values())
        self.search_button = search_button
        self.check_row_order = check_row_order
        self.active_color = active_color
        self.default_drag_direction = drag_direction

        self.row_min = 1
        self.row_max = len(self.known_rows)
        self.cur_min = 1
        self.cur_max = 1
        self.cur_buttons: list[OcrResultButton] = []

    def keyword2index(self, row: Keyword) -> int:
        """
        Args:
            row: Keyword
        Return: 
            int: index of Keyword among known_rows
        """
        try:
            return self.known_rows.index(row) + 1
        except ValueError:
            # logger.warning(f'Row "{row}" does not belong to {self}')
            return 0

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
            .matched_ocr(main.device.image, self.keyword_class)
        # Get indexes
        indexes = [self.keyword2index(row.matched_keyword)
                   for row in self.cur_buttons]
        indexes = [index for index in indexes if index]
        # Check row order
        if self.check_row_order and len(indexes) >= 2:
            if not np.all(np.diff(indexes) > 0):
                logger.warning(
                    f'Rows given to {self} are not ascending sorted')
        if not indexes:
            logger.warning(f'No valid rows loaded into {self}')
            return

        self.cur_min = min(indexes)
        self.cur_max = max(indexes)
        logger.attr(self.name, f'{self.cur_min} - {self.cur_max}')

    def drag_page(self, direction: str, main: AetherGazerHelper, vector=None):
        """
        Args:
            direction: up, down, left, right
            main:
            vector (tuple[float, float]): Specific `drag_vector`, None by default to use `self.drag_vector`
        """
        if vector is None:
            vector = self.drag_vector
        vector = np.random.uniform(*vector)
        width, height = self.search_button.width, self.search_button.height
        if direction == 'up':
            vector = (0, vector * height)
        elif direction == 'down':
            vector = (0, -vector * height)
        elif direction == 'left':
            vector = (vector * width, 0)
        elif direction == 'right':
            vector = (-vector * width, 0)
        else:
            logger.warning(f'Unknown drag direction: {direction}')
            return
        
        # p1, p2 = random_rectangle_vector_opted(vector, box=self.search_button.button)
        # main.device.drag(p1, p2, name=f'{self.name}_DRAG')

    def reverse_direction(self, direction):
        if direction == 'up':
            return 'down'
        if direction == 'down':
            return 'up'
        if direction == 'left':
            return 'right'
        if direction == 'right':
            return 'left'

    def insight_row(self, row: Keyword, main: AetherGazerHelper, skip_first_screenshot=True, blind=False) -> bool:
        """
        Args:
            row:
            main:
            skip_first_screenshot:

        Returns:
            If success
        """
        if not blind:
            row_index = self.keyword2index(row)
            if not row_index:
                logger.warning(f'Insight row {row} but index unknown')
                return False

            logger.info(f'Insight row: {row}, index={row_index}')
        last_buttons: set[OcrResultButton] = None
        bottom_check = Timer(3, count=5).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                main.device.screenshot()

            self.load_rows(main=main)

            # End
            if self.cur_buttons:
                if not blind and self.cur_min <= row_index <= self.cur_max:
                    break
                if blind and any(row.name == self.cur_buttons.name):
                    # 如果列表的元素是不定期改变的话，就不能用固定的下标去判断
                    break

            # Drag pages
            if not blind:
                if row_index < self.cur_min:
                    self.drag_page(self.reverse_direction(self.default_drag_direction), main=main)
                elif self.cur_max < row_index:
                    self.drag_page(self.default_drag_direction, main=main)
            else:
                self.drag_page(self.default_drag_direction, main=main)

            # Wait for bottoming out
            main.wait_until_stable(self.search_button, timer=Timer(
                0, count=0), timeout=Timer(1.5, count=5))
            skip_first_screenshot = True
            if self.cur_buttons and last_buttons == set(self.cur_buttons):
                if bottom_check.reached():
                    logger.warning(f'No more rows in {self}')
                    return False
            else:
                bottom_check.reset()
            last_buttons = set(self.cur_buttons)

        return True

    def is_row_selected(self, button: OcrResultButton, main: AetherGazerHelper) -> bool:
        # Having gold letters
        if main.image_color_count(button, color=self.active_color, threshold=221, count=50):
            return True

        return False

    def get_selected_row(self, main: AetherGazerHelper) -> Optional[OcrResultButton]:
        """
        `load_rows()` must be called before `get_selected_row()`.
        """
        for row in self.cur_buttons:
            if self.is_row_selected(row, main=main):
                return row
        return None

    def select_row(self, row: Keyword, main: AetherGazerHelper, insight=True, skip_first_screenshot=True):
        """
        Args:
            row:
            main:
            insight: If call `insight_row()` before selecting
            skip_first_screenshot:

        Returns:
            If success
        """
        if insight:
            result = self.insight_row(
                row, main=main, skip_first_screenshot=skip_first_screenshot)
            if not result:
                return False

        logger.info(f'Select row: {row}')
        skip_first_screenshot = True
        interval = Timer(5)
        skip_first_load_rows = True
        load_rows_interval = Timer(1)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                main.device.screenshot()

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

            # End
            if self.is_row_selected(button, main=main):
                logger.info(f'Row selected at {row}')
                return True

            # Click
            if interval.reached():
                main.device.click(button)
                interval.reset()
