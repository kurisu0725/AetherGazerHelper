from zafkiel import logger
from typing import Dict
from config.config import BaseConfig

class AetherGazerLogger(logger):
    def __init__(self, config : Dict = {}):
        super().__init__(config)
        self.config = config


    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config


def task_info(task_str):
    logger.info("######################################################")
    logger.info(f"-------------------{task_str}----------------------")
    logger.info("######################################################")
