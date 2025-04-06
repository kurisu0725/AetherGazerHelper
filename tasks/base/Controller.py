from zafkiel import find_click, exists, touch, sleep, auto_setup
from airtest.core.helper import G

class Controller:
    def __init__(self):
        self.screenshot = None
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
        if G.DEVICE is None:
            return False
        return True