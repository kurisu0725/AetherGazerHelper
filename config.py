import json
from pathlib import Path
from typing import Literal, List, Union
from pydantic import BaseModel, Field

class Item(BaseModel):
    """
    Minimum setting
    """
    type: Literal['input', 'select', 'checkbox', 'folder', 'file', 'priority'] = 'input'
    value: Union[str, bool, float]
    option: List[str] = []
    hidden: bool = False
    help: str = ''
    disabled: bool = False

    model_config = {
        'populate_by_name': True,
    }

    def __init__(self, value=None, **data):
        if value is not None and not isinstance(value, dict):
            data['value'] = value
        super().__init__(**data)

class GroupCustomBase(BaseModel):
    """
    Basic settings for every task
    """
    # active: Item = Item(type='checkbox', value=True)
    priority: Item = Item(type='priority', value=0)
    command: Item = Item('')

class TaskGeneral(BaseModel):
    class GroupGeneralBase(BaseModel):
        """
        General settings for the project
        """
        language: Item = Item('中文')
        work_dir: Item = Item('./repos/AetherGazerHelper')
        background: Item = Item(value=False, disabled=True)
        config_path: Item = Item('./repos/AetherGazerHelper/config/config.json')

    class GroupGame(BaseModel):
        game_path: Item = Item(type='file', value='E:\\AetherGazer\\AetherGazerStarter\\AetherGazer\\AetherGazer.exe')
        log_retain: Item = Item(type='select', value='1week', option=['1day', '3days', '1week', '1month'])

    Base: GroupGeneralBase = Field(GroupGeneralBase(), alias='_Base')
    Game: GroupGame = GroupGame()

class TaskLogin(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t login'), priority=Item(value=31, disabled=True)
    ), alias='_Base')

class TaskMail(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t mail'), priority=Item(value=6, disabled=True)
    ), alias='_Base')

class TaskMission(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t mission'), priority=Item(value=5, disabled=True)
    ), alias='_Base')

class TaskDorm(BaseModel):
    class GroupCombat(BaseModel):
        enable_combat : Item = Item(type="checkbox", value=True)
        weekly_combat_count : Item = Item(type="input", value=0.0, hidden=False, disabled=True)
        last_combat_time : Item = Item(type="input", value="", hidden=False, disabled=True)

    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t dorm'), priority=Item(value=7, disabled=True)
    ), alias='_Base')

    Combat : GroupCombat = GroupCombat()

class TaskGuild(BaseModel):
    class GroupGuildStore(BaseModel):
        enable_purchase_guild_store : Item = Item(type="checkbox", value=True)
        last_purchase_guild_store_time : Item = Item(type="input", value="", hidden=True)

    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t guild'), priority=Item(value=8, disabled=True)
    ), alias='_Base')

    Guild_Store : GroupGuildStore = GroupGuildStore()

class TaskStore(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t store'), priority=Item(value=9, disabled=True)
    ), alias='_Base')

class TaskMimir(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t mimir'), priority=Item(value=9, disabled=True)
    ), alias='_Base')

class TaskDaily(BaseModel):
    Base: GroupCustomBase = Field(GroupCustomBase(
        command=Item('py main.py -t daily'), priority=Item(value=10, disabled=True)
    ), alias='_Base')

#任务组级别
class MenuProject(BaseModel):
    General: TaskGeneral = TaskGeneral()  

class MenuBasic(BaseModel):
    Login: TaskLogin = TaskLogin()
    Mail: TaskMail = TaskMail()
    Dorm: TaskDorm = TaskDorm()
    Guild: TaskGuild = TaskGuild()
    Store: TaskStore = TaskStore()
    Mimir: TaskMimir = TaskMimir()
    Mission: TaskMission = TaskMission()
    Daily: TaskDaily = TaskDaily()

#项目级别
class UIContent(BaseModel):
    Project: MenuProject = MenuProject()
    Basic: MenuBasic = MenuBasic()


class Config:

    def __init__(self, config_path):
        self.config_path = config_path
        with open('config/template.json', 'r', encoding='utf-8') as f:
            args = json.load(f)
        with open(config_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        # 只是为了校验数据
        for menu, tasks in args.items():
            for task, groups in tasks.items():
                for group, items in groups.items():
                    if group == '_Base':
                        continue
                    for item, info in items.items():
                        info['value'] = self.data[menu][task][group][item]
        UIContent.model_validate(args)

    def update(self, menu, task, group, item, value):
        self.data[menu][task][group][item] = value
        with open(self.config_path, 'w') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

def gen_i18n(lang: str):
    import anyconfig
    
    trans_path = f"./config/i18n/{lang}.json"
    template_path = "./config/template.json"

    trans = {
        "Project": {
            "tasks": {
                "General": {
                    "groups": {}
                }
            }
        }
    }
    with open(template_path, 'r', encoding='utf-8') as f:
        tpl = anyconfig.load(f)

    for menu_name, menu_conf in tpl.items():
        if menu_name == "Project":
            if "General" in menu_conf.keys():

                group_trans = trans["Project"]["tasks"]["General"]["groups"]
                for group_name, group_conf in menu_conf["General"].items():
                    if group_name == "_Base":
                        continue
                    group_trans[group_name] = {
                            "name": group_name,
                            "help": group_conf.get("_help", {}).get("value", ""),
                            "items": {}
                        }
                    
                    item_trans = group_trans[group_name]["items"]
                    for item_name, item_conf in group_conf.items():
                        if item_name == "_help":
                            continue
                        item_trans[item_name] = {
                                "name": item_name,
                                "help": item_conf.get("help", ""),
                            }
                        for option_name in item_conf.get("option", []):
                            item_trans[item_name].setdefault("options", {})[option_name] = option_name
        else:
            trans[menu_name] = {
                "name": menu_name,
                "tasks": {}
            }

            task_trans = trans[menu_name]["tasks"]
            for task_name, task_conf in menu_conf.items():
                task_trans[task_name] = {
                    "name": task_name,
                    "groups": {}
                }

                group_trans = task_trans[task_name]["groups"]
                for group_name, group_conf in task_conf.items():
                    if group_name == "_Base":
                        continue
                    group_trans[group_name] = {
                        "name": group_name,
                        "help": group_conf.get("_help", {}).get("value", ""),
                        "items": {}
                    }

                    item_trans = group_trans[group_name]["items"]
                    for item_name, item_conf in group_conf.items():
                        if item_name == "_help":
                            continue
                        item_trans[item_name] = {
                            "name": item_name,
                            "help": item_conf.get("help", "")
                        }
                        for option_name in item_conf.get("option", []):
                            item_trans[item_name].setdefault("options", {})[option_name] = option_name

    if Path(trans_path).exists():
        with open(trans_path, 'r', encoding='utf-8') as f:
            old_trans = anyconfig.load(f)
        anyconfig.merge(trans, old_trans)

    with open(trans_path, 'w', encoding='utf-8') as f:
        anyconfig.dump(trans, f, ensure_ascii=False, indent=2, allow_unicode=True)

def export() -> None:
    args = UIContent()
    with open('config/template.json', 'w', encoding='utf-8') as f:
        f.write(args.model_dump_json(indent=2, by_alias=True))

if __name__ == "__main__":
    export()
