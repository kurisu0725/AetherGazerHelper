import time
import shutil
import datetime

from zafkiel import logger
from zafkiel.ui import UI
from typing import Dict
from pathlib import Path
from tasks.base.popup import popup_list
from tasks.base.Controller import Controller

class AetherGazerHelper(UI):
    def __init__(self, config : Dict = None):
        self.config = config or {}
        self._ops = Controller()
        self.process_str = self.config['General']['Game']['game_process_str']
        self.get_popup_list(popup_list)

        if self.check_device() == False:
           self.connect_device()

    def app_stop(self):
        self.stop_app()

    def app_start(self):
        pass

    def app_restart(self):
        self.app_stop()
        self.app_start()
        
    def manage_log(self):
        log_retain_map = {
            '1day': 1,
            '3days': 3,
            '1week': 7,
            '1month': 30,
        }
        retain_days = log_retain_map.get(self.config['General']['Game']['log_retain'], 7)

        current_time = time.time()
        log_path = Path('./log')

        for log_dir in log_path.iterdir():
            create_time = log_dir.stat().st_ctime
            age_in_days = (current_time - create_time) / (24 * 3600)

            if age_in_days > retain_days:
                try:
                    logger.info(f'Deleting old log directory: {log_dir}')
                    shutil.rmtree(log_dir)
                except Exception as e:
                    logger.error(f'Failed to delete {log_dir}: {e}')

    def run(self):
        pass

    def connect_device(self):
        logger.info(f'start connect to device')
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={self.process_str}", ])

    def find_click(self, *args, **kwargs):
        """
        Find and click on the specified element(s).
        """
        return self._ops.find_click(*args, **kwargs)

    def exists(self, *args, **kwargs):
        """
        Check if the specified element(s) exist.
        """
        return self._ops.exists(*args, **kwargs)
    
    def touch(self, *args, **kwargs):
        """
        Touch the specified element(s).
        """
        return self._ops.touch(*args, **kwargs)
    
    def sleep(self, *args, **kwargs):
        """
        Sleep for the specified duration.
        """
        return self._ops.sleep(*args, **kwargs)
    
    def check_device(self):
        """
        Check if the device is connected.
        """
        return self._ops.check_device()

    def auto_setup(self, *args, **kwargs):
        """
        Automatically set up the environment.
        """
        return self._ops.auto_setup(*args, **kwargs)


        



