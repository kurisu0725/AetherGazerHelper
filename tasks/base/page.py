from zafkiel import Template
from zafkiel.ocr import Keyword
from zafkiel.ui import Page

from tasks.base.assets.assets_page import *
from tasks.dispatch_room.assets.assets_dispatch_room import *
from tasks.base.switch import *

# 主界面
page_main = Page(MAIN_FLAG)

# 公共区 界面
page_public_area = Page(PUBLIC_AREA)

# 调度室界面
page_dispatch_room = Page(DISPATCH_ROOM)

# 调度收益界面
page_dispatch_reward = Page(DISPATCH_REWARD_FLAG, switch=switch_dispatch_reward)


# 建立有向边

# from 主界面 to
page_main.link(button=TO_PUBLIC_AREA, destination=page_public_area)

# from 公共区 to
page_public_area.link(button=TO_DISPATCH_ROOM, destination=page_dispatch_room)


# from 调度室 to 
page_dispatch_room.link(button=TO_DISPATCH_REWARD, destination=page_dispatch_reward)

# from 调度收益 to 