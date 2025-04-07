import time
import shutil
import datetime

from zafkiel import logger
from zafkiel.ui import UI
from typing import Dict
from pathlib import Path
from tasks.base.popup import popup_list
from module.Controller import Controller

class AetherGazerHelper(UI):
    def __init__(self, config : Dict = None):
        self.config = config or {}
        self.controller = Controller()
        self.process_str = self.config['General']['Game']['game_process_str']
        self.get_popup_list(popup_list)

        logger.info(f'init {self.process_str}')
        checkStatus = self.check_device()
        logger.info(f'check device status: {checkStatus}')

        if checkStatus == False:
            self.connect_device()
            logger.info(f'connect to device {self.process_str}')

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
        return self.controller.find_click(*args, **kwargs)

    def exists(self, *args, **kwargs):
        """
        Check if the specified element(s) exist.
        """
        return self.controller.exists(*args, **kwargs)
    
    def touch(self, *args, **kwargs):
        """
        Touch the specified element(s).
        """
        return self.controller.touch(*args, **kwargs)
    
    def sleep(self, *args, **kwargs):
        """
        Sleep for the specified duration.
        """
        return self.controller.sleep(*args, **kwargs)
    
    def check_device(self):
        """
        Check if the device is connected.
        """
        return self.controller.check_device()

    def auto_setup(self, *args, **kwargs):
        """
        Automatically set up the environment.
        """
        return self.controller.auto_setup(*args, **kwargs)


        



