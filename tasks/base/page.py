from zafkiel import Template
from zafkiel.ocr import Keyword
from zafkiel.ui import Page

from tasks.base.assets.assets_page import *
from tasks.dispatch_room.assets.assets_dispatch_room import *
from tasks.base.switch import *
from tasks.team.assets.assets_team import *
from tasks.base.assets.assets_share import *
from tasks.entrust.assets.assets_entrust import *

# 主界面
page_main = Page(MAIN_FLAG)

# 公共区 界面
page_public_area = Page(PUBLIC_AREA)

# 调度室界面
page_dispatch_room = Page(DISPATCH_ROOM)

# 调度收益界面
page_dispatch_reward = Page(DISPATCH_REWARD_FLAG, switch=switch_dispatch_reward)

# 班组界面
page_team = Page(TEAM_FLAG)

# 班组-补给界面
page_supply = Page(SUPPLY_FLAG)

# 委托界面
page_entrust = Page(ENTRUST_FLAG)

#----------- 建立有向边 -------------

# from 主界面 to
page_main.link(button=TO_PUBLIC_AREA, destination=page_public_area)
page_main.link(button=TO_TEAM, destination=page_team)
page_main.link(button=TO_ENTRUST, destination=page_entrust)

# from 公共区 to
page_public_area.link(button=TO_DISPATCH_ROOM, destination=page_dispatch_room)
page_public_area.link(button=BACK_CLICK, destination=page_main)
page_public_area.link(button=BACK_TO_MAIN_CLICK, destination=page_main)

# from 调度室 to 
page_dispatch_room.link(button=TO_DISPATCH_REWARD, destination=page_dispatch_reward)
page_dispatch_room.link(button=BACK_CLICK, destination=page_public_area)
page_dispatch_room.link(button=BACK_TO_MAIN_CLICK, destination=page_main)


# from 调度收益 to 
page_dispatch_reward.link(button=BACK_CLICK, destination=page_dispatch_room)
page_dispatch_reward.link(button=BACK_TO_MAIN_CLICK, destination=page_main)

# from 班组 to
page_team.link(button=TO_SUPPLY, destination=page_supply)
page_team.link(button=BACK_CLICK, destination=page_main)
page_team.link(button=BACK_TO_MAIN_CLICK, destination=page_main)

# from 班组—补给界面 to
page_supply.link(button=BACK_CLICK, destination=page_team)
page_supply.link(button=BACK_TO_MAIN_CLICK, destination=page_main)

# from 委托界面 to
page_entrust.link(button=BACK_CLICK, destination=page_main)
page_entrust.link(button=BACK_TO_MAIN_CLICK, destination=page_main)

