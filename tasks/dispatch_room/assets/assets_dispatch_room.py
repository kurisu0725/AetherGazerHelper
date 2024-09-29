from zafkiel import Template
from zafkiel.ocr import Keyword

# 主界面 TO 公共区的按钮
TO_PUBLIC_AREA = Template(r"TO_PUBLIC_AREA.png", (0.430, -0.03), Keyword('公共区'))
# 公共区界面的标志
PUBLIC_AREA = Template(r"PUBLIC_AREA.png", (-0.386, -0.090), Keyword('调度室'))

# 公共区界面 调度室的按钮
TO_DISPATCH_ROOM = Template(r"TO_DISPATCH_ROOM.png", (-0.386, -0.090), Keyword('调度室'))

# 调度室 界面的标志
DISPATCH_ROOM = Template(r"DISPATCH_ROOM.png", (-0.176, 0.233), rgb=True)

# from 调度室 to 调度收益界面 
TO_DISPATCH_REWARD = Template(r"TO_DISPATCH_REWARD.png", (0.101, 0.233), Keyword('调度收益'))

# 调度收益界面标志
DISPATCH_REWARD_FLAG = Template(r"DISPATCH_REWARD_FLAG.png", (-0.453, 0.216), rgb=True)

# 调度收益 -> 情报储备 Switch下的 "当前储存" 的体力数值
DISPATCH_REWARD_INTELLIGENCE_RESERVE_VALUE = Template(r"DISPATCH_REWARD_INTELLIGENCE_RESERVE_VALUE.png", (0.418, -0.131))

# 调度收益 -> 情报储备 Switch下的 "最大" 按钮
DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_ON = Template(r"DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_ON.png", (0.387, 0.184), rgb=True)
DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_OFF = Template(r"DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_OFF.png", (0.387, 0.184), rgb=True)

# 调度收益 -> 情报储备 Switch下的 "取出" 按钮
DISPATCH_REWARD_INTELLIGENCE_RESERVE_TAKE_OUT = Template(r"DISPATCH_REWARD_INTELLIGENCE_RESERVE_TAKE_OUT.png", (0.107, 0.222), Keyword('取出'))