from typing import Optional
from zafkiel import Template
from zafkiel.ocr.ocr import OcrResultButton
from zafkiel.ocr import Keyword
from zafkiel import logger
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
        drag_direction: str = "down"
    ):
        """
        Args:
            name:
            keyword_class: Keyword
            search_button:
            drag_direction: Default drag direction to higher index
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
        self.drag_direction = drag_direction

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