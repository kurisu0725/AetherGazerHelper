from zafkiel import logger
from typing import Dict
from config import BaseConfig

def task_info(task_str):
    logger.info("######################################################")
    logger.info(f"-------------------{task_str}----------------------")
    logger.info("######################################################")
