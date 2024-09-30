import argparse
import ctypes
import datetime
import json
import sys
from pathlib import Path

from loguru import logger
from zafkiel import API, simple_report

from tasks.login.login import Login
from tasks.dispatch_room.dispatch_room import DispatchRoom

logger.remove()
logger.add(sys.stdout, level="INFO", format="<green>{time:HH:mm:ss}</green> | "
                                            "<level>{level: <7}</level> | "
                                            "<level>{message}</level>",
           )
date = datetime.datetime.now().strftime("%Y-%m-%d")
logger.add(f'./log/{date}/{date}.log', level="DEBUG", format="<green>{time:HH:mm:ss}</green> | "
                                                             "<level>{level: <7}</level> | "
                                                             "<level>{message}</level>",
           )


def all_tasks(config):
    try:
        # # 日常
        Login(config).app_start()
        # DispatchRoom(config).run()
    except Exception as e:
        logger.exception(e)
        raise

    finally:
        simple_report(__file__, log_path=Path(f'./log/{date}/report').resolve(), output=f'./log/{date}/report.html')




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', '-t',
                        choices=["armada", "dorm_bonus", "errand", "expedition", "login", "logout", "mail",
                                 "mission", "sweep"],
                        help='Task name, one of "armada, dorm_bonus, errand, expedition, login, logout, mail, '
                             'mission, sweep"')
    parser.add_argument('--config_path', '-c', default='./config/config.json')
    args = parser.parse_args()

    if args.task:
        config_path = Path(args.config_path).resolve()
        if not config_path.exists():
            logger.error(f'{config_path} not found')
            return
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        # single_task(config, args.task)
    else:
        with open('./config/default.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        all_tasks(config)


if __name__ == '__main__':
    # 以管理员身份运行
    # if ctypes.windll.shell32.IsUserAnAdmin():
    #     main()
    # else:
    #     ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)
    from tasks.team.team  import  test_function
    test_function()