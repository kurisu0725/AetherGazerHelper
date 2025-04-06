from zafkiel import Template
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

BACK_BUTTON = Template(
    filename=r"BACK_BUTTON.png",
    record_pos=(-0.4583, -0.2505), 
    resolution=(1920, 1080), 
    rgb=False, 
    template_path="assets/share/base/page",
)

BACK_BUTTON_2 = Template(
    filename=r"BACK_BUTTON_2.png",
    record_pos=(-0.4562, -0.25), 
    resolution=(1920, 1080), 
    rgb=False, 
    template_path="assets/share/base/page",
)

BACK_TO_MAIN = Template(
    filename=r"BACK_TO_MAIN.png",
    record_pos=(-0.3990, -0.2510), 
    resolution=(1920, 1080), 
    threshold=0.4,
    rgb=False, 
    template_path="assets/share/base/page",
)