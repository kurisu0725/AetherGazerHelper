from zafkiel.ui import UI
from typing import Dict
from zafkiel import Template, logger, Timer
from zafkiel.exception import LoopError
from utils.logger_func import task_info

class Entrust(UI):
    def __init__(self, config: Dict = None):
        self.config = config

    def claim_reward(self):
        pass