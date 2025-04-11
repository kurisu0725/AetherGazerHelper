from zafkiel import Template
from zafkiel.ocr import Keyword
from module.page import Page

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

# 邮件界面
page_mail = Page(MAIL_CHECK)

# 宿舍界面
page_dorm = Page(DORM_CHECK) 

# 宿舍-导航 
page_dorm_nav = Page(DORM_NAV_CHECK)

# 宿舍-厨房
page_dorm_nav_kitchen = Page(DORM_NAV_KITCHEN_CHECK)

# 宿舍-修正者训练
page_dorm_nav_character = Page(DORM_NAV_CHARACTER_CHECK)

# 战令
page_battle_pass = Page(BATTLE_PASS_CHECK)

# 战令-任务
page_battle_pass_mission = Page(BATTLE_PASS_MISSION_CHECK)

# 活动入口
page_activity = Page(ACTIVITY_CHECK)

# 活动-联防协议

# 日常资源界面
page_resource = Page(RESOURCE_CHECK, switch=switch_resource)


# from page_main to 
page_main.link(MAIN_TO_GUILD, destination=page_guild)
page_main.link(MAIN_TO_MIMIR, destination=page_mimir)
page_main.link(MAIN_TO_STORE, destination=page_store)
page_main.link(MAIN_TO_MISSION, destination=page_mission)
page_main.link(MAIN_TO_MAIL, destination=page_mail)
page_main.link(MAIN_TO_DORM, destination=page_dorm)
page_main.link(MAIN_TO_BATTLE_PASS, destination=page_battle_pass)
page_main.link(MAIN_TO_ACTIVITY, destination=page_activity, blind_to_click=True)
page_main.link(MAIN_TO_RESOURCE, destination=page_resource)

# from page_mimir to mimir observation
page_mimir.link(MIMIR_TO_MIMI_OBSERVATION, destination=page_mimi_observation)

# from page_mimi_observation to
page_mimi_observation.link(BACK_BUTTON, destination=page_mimir)
page_mimi_observation.link(BACK_TO_MAIN, destination=page_main)

# from page_store to
page_store.link(STORE_TO_STORE_SUPPLY, destination=page_store_supply)
page_store.link(BACK_TO_MAIN, destination=page_main)

# from page_store_supply to
page_store_supply.link(BACK_BUTTON, destination=page_store)
page_store_supply.link(BACK_TO_MAIN, destination=page_main)

# from page_mission to
page_mission.link(BACK_TO_MAIN, destination=page_main)


# from page_mail to
page_mail.link(BACK_TO_MAIN, destination=page_main)

# from page_guild to
page_guild.link(BACK_BUTTON, destination=page_main)
page_guild.link(BACK_TO_MAIN, destination=page_main)

# from page_dorm to
page_dorm.link(BACK_TO_MAIN, destination=page_main)
page_dorm.link(DORM_TO_DORM_NAV, destination=page_dorm_nav)

# from page_dorm_nav to
page_dorm_nav.link(DORM_NAV_TO_DORM_NAV_CHARACTER, destination=page_dorm_nav_character)
page_dorm_nav.link(DORM_NAV_TO_DORM_NAV_KITCHEN, destination=page_dorm_nav_kitchen)

# from page_dorm_nav_kitchen to
page_dorm_nav_kitchen.link(BACK_BUTTON, destination=page_dorm)
page_dorm_nav_kitchen.link(BACK_TO_MAIN, destination=page_main)
page_dorm_nav_kitchen.link(DORM_NAV_KITCHEN_TO_DORM_NAV, destination=page_dorm_nav)

# from page_dorm_nav_character to
page_dorm_nav_character.link(BACK_BUTTON, destination=page_dorm)
page_dorm_nav_character.link(BACK_TO_MAIN, destination=page_main)

# from page_battle_pass to
page_battle_pass.link(BACK_BUTTON, destination=page_main)
page_battle_pass.link(BACK_TO_MAIN, destination=page_main)
page_battle_pass.link(BATTLE_PASS_TO_BATTLE_PASS_MISSION, destination=page_battle_pass_mission)

# from page_battle_pass_mission to
page_battle_pass_mission.link(BACK_BUTTON, destination=page_battle_pass)
page_battle_pass_mission.link(BACK_TO_MAIN, destination=page_main)


# from page_activity to
page_activity.link(BACK_BUTTON, destination=page_main)


# from page_resource to
page_resource.link(BACK_TO_MAIN, destination=page_main)