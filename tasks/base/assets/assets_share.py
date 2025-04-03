from zafkiel import API, Template
from zafkiel.ocr import Keyword

GET_ITEM = Template(
    filename=r"GET_ITEM.png",
    record_pos=(0.00, -0.13), 
    keyword=Keyword(u'获得物品'),
    resolution=(1600, 900) , 
    rgb=False, 
    template_path="assets/share/claim",
)

CLICK_TO_CONTINUE = Template(
    filename=r"CLICK_TO_CONTINUE.png",
    record_pos=(0.00, 0.24), 
    keyword=Keyword(u'点击屏幕继续'),
    resolution=(1600, 900) , 
    rgb=False, 
    template_path="assets/share/claim",
)
