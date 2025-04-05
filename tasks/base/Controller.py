from zafkiel import find_click, exists, touch, sleep, auto_setup

class Controller:
    def __init__(self):
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