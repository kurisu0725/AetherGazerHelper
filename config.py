import json
from pathlib import Path
from typing import Literal, List, Union
from pydantic import BaseModel, Field


class Config:

    def __init__(self, config_path):
        self.config_path = config_path
    

    def update(self, menu, task, group, item, value):
        pass

def export() -> None:
    pass

if __name__ == "__main__":
    export()
