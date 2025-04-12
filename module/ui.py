from zafkiel import exists, Template, app_is_running, touch, screenshot
from zafkiel.logger import logger
from zafkiel.ocr.ocr import Ocr
from module.page import Page
from zafkiel.decorator import run_once
from zafkiel.exception import NotRunningError, PageUnknownError, ScriptError
from zafkiel.timer import Timer
from zafkiel.ui.switch import Switch
from typing import Union

class UI:
    """
    Processing interface related functions.
    Main code comes from https://github.com/LmeSzinc/StarRailCopilot/blob/master/tasks/base/ui.py
    and https://github.com/LmeSzinc/StarRailCopilot/blob/master/module/ui/switch.py
    """

    # Make ui_current mutable so that it can be shared among subclasses of the UI class.
    ui_current: dict = {'page': None}
    popup_list: list = []

    def ui_switch_appear(self, switch: Switch) -> bool:
        """
        Args:
            switch:
        """
        if self.ui_get_current_page().switch != switch:
            return False

        for data in switch.state_list:
            if exists(data['check_button']):
                return True
        return False

    def ui_get_current_state(self, switch: Switch) -> str:
        """
        Args:
            switch:

        Returns:
            state name or 'unknown'.
        """
        if self.ui_current['page'].switch != switch:
            logger.warning(f"{self.ui_current['page']} does not have {switch}")
            return 'unknown'

        for data in switch.state_list:
            if exists(data['check_button']):
                return data['state']
        return 'unknown'

    @staticmethod
    def ui_page_appear(page: Page, timeout: float = 0) -> Union[bool , tuple]:
        """
        Args:
            page:
            timeout: Seconds to find.

        Returns:
            If found, return tuple of (x, y), else return False.
        """
        return exists(page.check_button, timeout)

    def ui_get_current_page(self, reload: bool = True):
        """
        Returns:
            Page:

        Raises:
            NotRunningError:
            PageUnknownError:
        """

        @run_once
        def app_check():
            if not app_is_running():
                raise NotRunningError("Game not running")
            
        if reload == False:
            if self.ui_current['page'] is not None :
                return self.ui_current['page']
            else:
                raise PageUnknownError("Unknown page")

        timeout = Timer(10, count=20).start()
        while True:

            # End
            if timeout.reached():
                break

            # Known pages
            for page in Page.iter_pages():
                if page.check_button is None:
                    continue
                if self.ui_page_appear(page=page):
                    self.ui_current['page'] = page
                    return page

            # Unknown page but able to handle
            if self.ui_additional():
                timeout.reset()
                continue

            app_check()

        # Unknown page, need manual switching
        raise PageUnknownError

    def _set_state(self, switch: Switch, state: Template) -> bool:
        counter = 0
        changed = False
        warning_show_timer = Timer(5, count=10).start()
        click_timer = Timer(1, count=3)
        while True:

            # Detect
            current = self.ui_get_current_state(switch)

            # End
            if current == state.name:
                logger.info(f'{switch.name} set to {state.name}')
                return changed

            # Warning
            if current == 'unknown':
                if self.ui_additional():
                    continue
                if warning_show_timer.reached():
                    logger.warning(f'Unknown {switch.name} switch')
                    warning_show_timer.reset()
                    if counter >= 1:
                        logger.warning(
                            f'{switch.name} switch {state.name} asset has evaluated to unknown too many times, '
                            f'asset should be re-verified')
                        return False
                    counter += 1
                continue

            # Click
            if click_timer.reached():
                click_state = state if switch.is_choice else current
                button = switch.get_data(click_state)['click_button']
                touch(button)
                click_timer.reset()
                changed = True

        return changed

    def ui_goto(self, destination: Page, state: Template = None):
        """
        Args:
            destination:
            state: Target state of switch, which must be in destination page.
        """

        # check if state is valid
        if state is not None:
            if destination.switch is None:
                raise ScriptError(f'Page {destination} has no switch')
            destination.switch.get_data(state)

            logger.debug(f">>> UI GOTO {str(destination).upper()}:{state.name.upper()}")
        else:
            logger.debug(f">>> UI GOTO {str(destination).upper()}")

        # Create connection
        Page.init_connection(destination)
        # logger.debug(Page.display_all_pages_parent())
        while True:

            # Destination page
            if self.ui_page_appear(destination, timeout=0.5):
                self.ui_current['page'] = destination
                logger.debug(f'Page arrive: {destination}')
                if state is not None:
                    self._set_state(destination.switch, state)
                break

            # Other pages
            clicked = False

            page = self.ui_get_current_page()
            logger.debug(f"page: {page}, parent: {page.parent}")
            # the button from page to page  like  page_main to page_activity, it is changeable, and i don't want to update this assets in  game's each version,
            # but it's pos always the same, so I need a blind click param
            if exists(page.check_button):
                button = page.links[page.parent]
                touch(button, blind=page.is_blind[page.parent]) # modified
                self.ui_current['page'] = page.parent
                logger.info(f'Page switch: {page} -> {page.parent}')
                clicked = True
        
            if clicked:
                continue

            # Additional
            if self.ui_additional():
                continue

        # Reset connection
        Page.clear_connection()

    def ui_ensure(self, destination: Page, state: Template = None) -> bool:
        """
        Args:
            destination:
            state: Target state of switch, which must be in destination page.

        Returns:
            bool: If UI switched.
        """
        self.ui_get_current_page()

        if self.ui_current['page'] == destination:
            if state is not None:
                if self.ui_get_current_state(destination.switch) == state.name:
                    logger.debug(f"Arrived at {destination}:{state.name}")
                    return False
                else:
                    self._set_state(destination.switch, state)
                    return True
            else:
                logger.debug(f"Already at {destination}")
                return False
        else:
            self.ui_goto(destination, state)
            return True

    def ui_ensure_index(
            self,
            index: int,
            letter: Union[Ocr, callable],
            next_button: Template,
            prev_button: Template,
            fast: bool = True,
            interval: float = 0.2
    ):
        """
        For pages with similar layout, ensure index of target page.

        Args:
            index: Index of target page.
            letter: OCR button.
            next_button:
            prev_button:
            fast: Default true. False when index is not continuous.
            interval: Seconds between two click.
        """
        retry = Timer(1, count=2)
        while True:
            if isinstance(letter, Ocr):
                current = letter.ocr_single_line(screenshot())
            else:
                current = letter(screenshot())

            logger.info(f"{self.ui_current['page']}: Index {current}")
            diff = index - current
            if diff == 0:
                break
            if current == 0:
                logger.warning(f'ui_ensure_index got an empty current value: {current}')
                continue

            if retry.reached():
                button = next_button if diff > 0 else prev_button
                if fast:
                    touch(button, times=abs(diff), interval=interval)
                else:
                    touch(button)
                retry.reset()

    def get_popup_list(self, popups: list):
        """
        Get list from program, must be called before self.ui_additional().

        Args:
            popups: list of handle popup functions
        """
        for popup in popups:
            self.popup_list.append(popup)

    def ui_additional(self) -> bool:
        """
        Handle all possible popups during UI switching.

        Returns:
            If handled any popup.
        """
        for popup in self.popup_list:
            if popup():
                return True

        return False

    def to_json(self) -> dict:
        # May not be actual current page
        return {'ui_current': str(self.ui_current['page'])}
