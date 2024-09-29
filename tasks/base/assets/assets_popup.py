from zafkiel import API, Template
from zafkiel.ocr import Keyword

NOTICE_FLAG = Template(r"NOTICE_FLAG.png", (-0.099, -0.169), Keyword('活动公告'))
NOTICE_CLOSE = Template(r"NOTICE_CLOSE.png", (0.347, -0.169))