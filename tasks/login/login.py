import subprocess
import datetime
import cv2
import time
import shutil
import psutil
import os

from zafkiel import logger
from pathlib import Path
from zafkiel.exception import LoopError
from typing import Dict
from tasks.base.page import *
from tasks.login.assets.assets_login import *
from tasks.base.AetherGazerHelper import AetherGazerHelper


class Login(AetherGazerHelper):
    def __init__(self, config: Dict) -> None:
        super().__init__(config)

    def app_start(self):
        game_path = self.config['General']['Game']['game_path']
        game_exe_name = os.path.basename(game_path)  # 获取游戏可执行文件名（如 "Game.exe"）

        # 检查游戏是否已经在运行
        is_game_running = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == game_exe_name:
                logger.info(f"Detect game is already running.")
                is_game_running = True
                break

        # 如果游戏未运行，则启动
        if not is_game_running:
            subprocess.Popen([game_path])

        self.connect_device()
        self.manage_log()

        self.sleep(10)
        self.handle_app_login()

    def app_restart(self):
        self.app_stop()
        self.app_start()
        self.handle_app_login()

    def handle_app_login(self):
        from utils.logger_func import task_info
        task_info('Login Program')

        logger.info("Handle_app_login.")

        find_res = self.find_click(LOGIN_CHECK, LOGIN_CHECK, times=5, interval=3, ocr_mode=0, local_search=True)
        if find_res == False:
            logger.error("Loop exceed time limit!")
            raise LoopError("Loop exceed time limit!")
        logger.debug(f"识别到登录界面")

        while True:

            if self.ui_page_appear(page_main, timeout=2):
                if not self.ui_ensure(page_main):
                    logger.info('游戏登录成功!')
                    break
            if self.ui_additional():
                continue
        return True

        

    def test(self):
        print("start test...................")
        self.app_start()
        
            


if __name__ == "__main__":
    pass
    