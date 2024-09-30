from zafkiel import Template
from zafkiel.ocr import Keyword

# 主界面-委托按钮
TO_ENTRUST = Template(r"TO_ENTRUST.png", (0.224, 0.250), Keyword(u'委托'))

# 委托界面 标志
ENTRUST_FLAG = Template(r"ENTRUST_FLAG.png", (-0.383, -0.201), Keyword(u'日活跃度报酬'))

# 委托界面 领取按钮
ENTRUST_CLAIM_ALL_CLICK = Template(r"ENTRUST_CLAIM_ALL_CLICK.png", (0.367, 0.232), Keyword(u'一键领取'))
