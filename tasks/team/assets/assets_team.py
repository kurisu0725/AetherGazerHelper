from zafkiel import Template
from zafkiel.ocr import Keyword

TEAM_FLAG = Template(r"TEAM_FLAG.png", (0.431, 0.207), Keyword(u'尘烟前线'))

TO_TEAM = Template(r"TO_TEAM.png", (0.280, 0.249), Keyword(u'班组'))

PRIORITY_CLICK = Template(r"PRIORITY_CLICK.png", (0.245, 0.248), Keyword(u'要务'))

# To 班组-补给界面
TO_SUPPLY = Template(r"TO_SUPPLY.png", (0.188, 0.248), Keyword(u'补给'))
# 班组-补给界面 标志
SUPPLY_FLAG = Template(r"SUPPLY_FLAG.png", (-0.418, -0.214), Keyword(u'班组领取记录'))
# 班组-补给界面 领取奖励

CLAIM_CLICK = Template(r"CLAIM_CLICK.png", (0.314, 0.232), Keyword(u'领取全部'))

# 班组-要务 '开始作战'按钮
PRIORITY_BEGIN_CLICK = Template(r"PRIORITY_BEGIN_CLICK.png", (0.245, 0.163), Keyword(u'开始作战'))

# 班组-要务 关闭按钮
PRIORITY_CLOSE = Template(r"PRIORITY_CLOSE.png", (0.341, -0.154), rgb=True)
