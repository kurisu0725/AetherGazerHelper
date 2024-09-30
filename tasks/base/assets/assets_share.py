from zafkiel import API, Template
from zafkiel.ocr import Keyword

# 返回按钮
BACK_CLICK = Template(r"BACK_CLICK.png", (-0.470, -0.255))

# 返回主界面按钮
BACK_TO_MAIN_CLICK = Template(r"BACK_TO_MAIN_CLICK.png", (-0.421, -0.254))

# 作战准备阶段 '作战开始'按钮
BATTLE_PREPARE_BEGIN_CLICK = Template(r"BATTLE_PREPARE_BEGIN_CLICK.png", (0.001, 0.231), Keyword(u'作战开始'))

# 战斗界面 一倍速按钮
BATTLE_NORMAL_SPEED = Template(r"BATTLE_NORMAL_SPEED.png", (0.424, -0.257), rgb=True)

# 战斗界面 2x按钮
BATTLE_DOUBLE_SPEED = Template(r"BATTLE_DOUBLE_SPEED.png", (0.423, -0.256), rgb=True)

# 战斗界面 3x按钮
BATTLE_TRIPLE_SPEED = Template(r"BATTLE_TRIPLE_SPEED.png", (0.423, -0.257), rgb=True)

# 战斗界面 auto关闭
BATTLE_AUTO_OFF = Template(r"BATTLE_AUTO_OFF.png", (0.380, -0.258), rgb=True)

# 战斗界面 auto开启
BATTLE_AUTO_ON = Template(r"BATTLE_AUTO_ON.png", (0.379, -0.257), rgb=True)

# 战斗界面 完成标志
BATTLE_COMPLETE_FLAG = Template(r"BATTLE_COMPLETE_FLAG.png", (0.332, -0.209), Keyword(u'任务完成'))

# 战斗完毕 确认
BATTLE_COMPLETE_CONFIRM = Template(r"BATTLE_COMPLETE_CONFIRM.png", (0.331, 0.232), Keyword(u'确认'))
