from zafkiel import Template
from zafkiel.ocr import Keyword
from zafkiel.ui import Page

from tasks.base.assets.assets_page import *
from tasks.base.switch import *
from tasks.base.assets.assets_share import *

# 主界面
page_main = Page(MAIN_CHECK)

# mimir界面
page_mimir = Page(MIMIR_CHECK)

# 弥弥观测站
page_mimi_observation = Page(MIMI_OBSERVATION_CHECK)

# 公会界面
page_guild = Page(GUILD_CHECK)

# 商店界面
page_store = Page(STORE_CHECK)

# 商店补给区界面
page_store_supply = Page(STORE_SUPPLY_CHECK)

# 任务界面
page_mission = Page(MISSION_CHECK, switch=switch_mission)


# from page_main to 
page_main.link(MAIN_TO_GUILD, destination=page_guild)
page_main.link(MAIN_TO_MIMIR, destination=page_mimir)
page_main.link(MAIN_TO_STORE, destination=page_store)
page_main.link(MAIN_TO_MISSION, destination=page_mission)


# from page_mimir to mimir observation
page_mimir.link(MIMIR_TO_MIMI_OBSERVATION, destination=page_mimi_observation)

# from page_mimi_observation to
page_mimi_observation.link(BACK_BUTTON, destination=page_mimir)
page_mimi_observation.link(BACK_TO_MAIN, destination=page_main)

# from page_store to
page_store.link(STORE_TO_STORE_SUPPLY, destination=page_store_supply)
page_store.link(BACK_BUTTON, destination=page_main)
page_store.link(BACK_TO_MAIN, destination=page_main)

# from page_store_supply to
page_store_supply.link(BACK_BUTTON, destination=page_store)
page_store_supply.link(BACK_TO_MAIN, destination=page_main)

# from page_mission to
page_mission.link(BACK_BUTTON_2, destination=page_main)
# page_mission.link(BACK_TO_MAIN, destination=page_main)
