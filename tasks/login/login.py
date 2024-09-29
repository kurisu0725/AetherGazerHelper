import subprocess
import datetime
import cv2
import time
import shutil

from zafkiel import Template, logger
from pathlib import Path
from zafkiel.ui import UI
from zafkiel.exception import LoopError
from typing import Dict
from tasks.base.popup import popup_list, popup_handler
from tasks.base.page import *
from tasks.login.assets.assets_login import LOGIN_FLAG, LOGIN_CLICK

class Login(UI):
    def __init__(self, config: Dict) -> None:
        super().__init__()
        self.config = config

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

    def app_stop(self):
        self.stop_app()

    def app_start(self):
        
        subprocess.Popen([self.config['General']['Game']['game_path']])
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        process_str = "少女前线2：追放"
        self.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
        self.manage_log()
        self.get_popup_list(popup_list)  # TODO: Move to program start instead of game start

        self.sleep(10)
        self.handle_app_login()

    def app_restart(self):
        self.app_stop()
        self.app_start()
        self.handle_app_login()

    def handle_app_login(self):
        from utils.logger_func import task_info
        task_info('Login Program')
        
        logger.info("Handle_app_login......")
        logger.debug(f"finding LOGIN_FLAG")
        find_res = self.find_click(LOGIN_FLAG, LOGIN_FLAG,
                   timeout=10, interval=3, ocr_mode=0,local_search=True)
        if find_res == False:
            raise LoopError("finding too many times")
        logger.debug(f"finding LOGIN_CLICK")
        self.find_click(LOGIN_CLICK, LOGIN_CLICK,
                   times=2, blind=False, interval=3, local_search=True)
        while True:
            if self.ui_additional():
                continue
            # if popup_handler.handle_abyss_settle():
            #     continue
            if self.ui_page_appear(page_main, timeout=5):
                self.sleep(3)
                if not self.ui_ensure(page_main):
                    logger.info('Game login successful')
                    break

        return True

    def test(self):
        print("start test...................")
        img = self.screenshot()
        cv2.imshow("screenshot", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite("capture_screenshot.png", img)
        
            


if __name__ == "__main__":
    import pygetwindow as gw
    img = cv2.imread()
    def print_open_window_titles():
        windows = gw.getAllTitles()
        for title in windows:
            print(title)

    print_open_window_titles()
    