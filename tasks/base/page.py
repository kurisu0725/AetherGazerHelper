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


# from page_main to 
page_main.link(MAIN_TO_GUILD, destination=page_guild)
page_main.link(MAIN_TO_MIMIR, destination=page_mimir)

# from page_mimir to mimir observation
page_mimir.link(MIMIR_TO_MIMI_OBSERVATION, destination=page_mimi_observation)

# from page_mimi_observation to
page_mimi_observation.link(BACK_BUTTON, destination=page_mimir)
page_mimi_observation.link(BACK_TO_MAIN, destination=page_main)

