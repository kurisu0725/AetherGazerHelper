import argparse
import ctypes
import datetime
import json
import sys
from pathlib import Path
from typing import Type
from zafkiel import simple_report, logger
from airtest.core.api import ST

from tasks import Login, Guild, Mimir, Daily, Store, Mission, Mail, Dorm
from module.Controller import Controller
from module.AetherGazerHelper import AetherGazerHelper
from config import Config

ST.OPDELAY = 0.3
ST.FIND_TIMEOUT = 10
ST.THRESHOLD = 0.65 # TODO: 写进config类中


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


class TaskFactory:
    _tasks = {
        'login': Login,
        'dorm': Dorm,
        'guild': Guild,
        'mimir': Mimir,
        'daily': Daily,
        'store': Store,
        'mission': Mission,
        'mail': Mail,
        'daily': Daily,
    }

    @classmethod
    def get_task(cls, task_name: str, config: Config, controller: Controller):
        task_class = cls._tasks.get(task_name)
        if not task_class:
            raise ValueError(f"Unknown task: {task_name}")
        return task_class(config, controller)

    @classmethod
    def register_task(cls, name: str, task_class: Type[AetherGazerHelper]):
        """动态注册新任务"""
        cls._tasks[name] = task_class

def all_tasks(config):

    try:
        logger.info(f"ST.OPDELAY : {ST.OPDELAY}, ST.FIND_TIMEOUT : {ST.FIND_TIMEOUT}, ST.THRESHOLD : {ST.THRESHOLD}")
        controller = Controller()
        # # 日常
        # Login(config, controller).run()
        # Guild(config, controller).run()
        # Dorm(config, controller).run()
        Mimir(config, controller).run()
        # Daily(config, controller).run()
        # Store(config, controller).run()
        # Mission(config, controller).run()
        # Mail(config, controller).run()
        
    except Exception as e:
        logger.exception(e)
        raise

    finally:
        simple_report(__file__, log_path=Path(f'./log/{date}/report').resolve(), output=f'./log/{date}/report.html')


def single_task(config, task):
    try:
       taskFactory = TaskFactory
       controller = Controller()
       cur_task = taskFactory.get_task(task, config, controller)
       cur_task.run()

    except Exception as e:
        simple_report(__file__, log_path=Path(f'./log/{date}/report').resolve(), output=f'./log/{date}/report.html')
        logger.error(e)
        raise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task', '-t',
                        choices=["login", "dorm", "guild", "store", "mail", "mission", "daily"],
                        help='Task name, one of "login, dorm, guild, store, mail, '
                             'mission, daily"')
    parser.add_argument('--config_path', '-c', default='./config/config.json')
    args = parser.parse_args()

    if args.task:
        config_path = Path(args.config_path).resolve()
        if not config_path.exists():
            logger.error(f'{config_path} not found')
            return
        # with open(config_path, 'r', encoding='utf-8') as f:
        #     config = json.load(f)
        # single_task(config, args.task)
        config = Config(config_path)
        single_task(config, args.task)
    else:
        config = Config('./config/default.json')
        all_tasks(config)


if __name__ == '__main__':
    from utils.test_program import run_as_admin
    # run_as_admin()
    try:
        main()  # 你的主函数
    except Exception as e:
        print(f"程序崩溃: {repr(e)}")
    
