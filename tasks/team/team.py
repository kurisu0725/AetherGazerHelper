from zafkiel.ui import UI
from typing import Dict
from zafkiel import Template, logger, Timer
from zafkiel.exception import LoopError
from tasks.base.page import page_team, page_supply
from tasks.team.assets.assets_team import *
from utils.logger_func import task_info

class Team(UI):
    def __init__(self, config: Dict = None):
        self.config = config


    def daily_battle(self):
        """
        To do: 
            完成 "要务" 
            find and click "要务" button, and complete a daily battle
        Return: bool
            判断是否完成 "要务"
            whether complete
        """
        logger.info("Start 'priority' process")

        while True:
            if self.find_click(PRIORITY_BEGIN_CLICK, blind=True):
                continue
            ### in_battle

            ### battle_complete

            ### 要务完成 标志,退出要务界面
            if self.exists():
                logger.info("Priority complete flag detected.")
                self.find_click(PRIORITY_CLOSE, blind=True)
                logger.info("Close priority page.")
                break



    def take_supply(self):
        """
        To do:
            claim supply reward
        """
        logger.info("Start claiming supply")
        self.ui_ensure(page_supply)

        timer = Timer(0, 10).start()
        while True:
            if timer.reached():
                raise LoopError('The operation has looped too many times')
            
            if self.find_click(CLAIM_CLICK):
                logger.info("Claim supply completed")
                break
            else:
                logger.info("Supply has been claimed")
                break
            
            

    def run(self):
        task_info("Team event")
        self.ui_ensure(page_team)
        self.take_supply()
        self.daily_battle()


def test_function():
    from utils.test_program import run_as_admin
    run_as_admin()
    from pathlib import Path
    import datetime
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    process_str = "少女前线2：追放"
    team = Team()
    team.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
    team.take_supply()