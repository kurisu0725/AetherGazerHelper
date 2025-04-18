import time
from airtest.core.helper import logwrap
from zafkiel import find_click, exists, touch, sleep, auto_setup, screenshot, swipe, loop_find
from airtest.core.helper import G
from airtest.core.settings import Settings as ST
from zafkiel.ocr.ocr import Ocr
from zafkiel.logger import logger
from zafkiel.utils import is_color_similar, crop
from airtest.core.cv import try_log_screen
from airtest.core.error import TargetNotFoundError

class Controller:
    def __init__(self):
        self.image = None
        pass

    def find_click(self, *args, **kwargs):
        """
        Find and click on the specified element(s).
        """
        return find_click(*args, **kwargs)
    

    def exists(self, *args, **kwargs):
        """
        Check if the specified element(s) exist.
        """
        return exists(*args, **kwargs)
    
    def touch(self, *args, **kwargs):
        """
        Touch the specified element(s).
        """
        return touch(*args, **kwargs)
    
    def sleep(self, *args, **kwargs):
        """
        Sleep for the specified duration.
        """
        return sleep(*args, **kwargs)
    
    def auto_setup(self, *args, **kwargs):
        """
        Automatically set up the environment.
        """
        return auto_setup(*args, **kwargs)

    def check_device(self):
        """
        Check if the device is connected.
        """
        if len(G.DEVICE_LIST) == 0:
            return False
        return True

    def swipe(self, *args, **kwargs):
        return swipe(*args, **kwargs)

    def screenshot(self):
        """
        Take a screenshot of the current screen.
        """
        self.image = screenshot()
        return self.image


    @logwrap
    def loop_find(
            self,
            v,
            timeout=ST.FIND_TIMEOUT,
            threshold=None,
            interval=0.02,
            interval_func=None,
            ocr_mode=0,
            cls=Ocr,
            local_search=True
    ):
        """
        Search for image template in the screen until timeout
        Add OCR and color similarity search to airtest.cv.loop_find()

        Args:
            v: image template to be found in screenshot
            timeout: time interval how long to look for the image template
            threshold: default is None
            interval: sleep interval before next attempt to find the image template
            interval_func: function that is executed after unsuccessful attempt to find the image template
            ocr_mode: Ocr match rules, one of `OCR_EQUAL`, `OCR_CONTAINS`, `OCR_SIMILAR`.
            cls: "Ocr" class or its subclass
            local_search: True if you only want to search for template image at the corresponding positions on the screen,
                otherwise it will search the entire screen.

        Raises:
            TargetNotFoundError: when image template is not found in screenshot

        Returns:
            TargetNotFoundError if image template not found, otherwise returns the position where the image template has
            been found in screenshot
        """
        start_time = time.time()
        while True:
            screen = G.DEVICE.snapshot(filename=None, quality=ST.SNAPSHOT_QUALITY)

            if screen is None:
                logger.warning("Screen is None, may be locked")
            else:
                if threshold:
                    v.threshold = threshold

                if not v.rgb or is_color_similar(v.image, crop(screen, v.area)):
                    if v.keyword is not None:
                        ocr = cls(v)
                        if ocr.ocr_match_keyword(screen, ocr.button.keyword, mode=ocr_mode):
                            match_pos = int((v.area[0] + v.area[2]) / 2), int((v.area[1] + v.area[3]) / 2)
                            try_log_screen(screen)
                            return match_pos
                    else:
                        match_pos = v.match_in(screen, local_search)
                        if match_pos:
                            cost_time = time.time() - start_time
                            logger.debug(f"ImgRec <{v.name}> cost {cost_time:.2f}s: {match_pos}")

                            try_log_screen(screen)
                            return match_pos

            if interval_func is not None:
                interval_func()

            if (time.time() - start_time) > timeout:
                logger.debug(f"<{v.name}> matching failed in {timeout}s")
                try_log_screen(screen)
                raise TargetNotFoundError(f'Picture {v.filepath} not found on screen')

            else:
                time.sleep(interval)

        