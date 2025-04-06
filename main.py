import argparse
import ctypes
import datetime
import json
import sys
from pathlib import Path

from zafkiel import simple_report, logger

from tasks.login.login import Login
from tasks.guild.guild import Guild
from tasks.mimir.mimir import Mimir
from tasks.daily.daily import Daily
from tasks.store.store import Store
from tasks.mission.mission import Mission
from airtest.core.settings import Settings as ST
ST.OPDELAY = 0
ST.FIND_TIMEOUT = 5
ST.THRESHOLD = 0.5 # TODO: 写进config类中


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
        # Login(config).app_start()
        # Guild(config).run()
        # Mimir(config).run()
        # Daily(config).run()
        Store(config).run()
        # Mission(config).run()
        
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
    from utils.test_program import run_as_admin
    # run_as_admin()
    try:
        main()  # 你的主函数
    except Exception as e:
        print(f"程序崩溃: {repr(e)}")
    
