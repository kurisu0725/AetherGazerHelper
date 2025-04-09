from zafkiel import Template
from zafkiel.ocr import Keyword

DORM_NAV_KITCHEN_CURRENCY_CLAIM = Template(
    filename=r"DORM_NAV_KITCHEN_CURRENCY_CLAIM.png", 
    record_pos=(-0.2375, 0.0203), 
    resolution=(1920, 1080),
    keyword=Keyword(u'可领取'),
    rgb=False, 
    template_path="assets/dorm",
)

DORM_NAV_KITCHEN_TASK_ASSIGN = Template(
    filename=r"DORM_NAV_KITCHEN_TASK_ASSIGN.png", 
    record_pos=(0.4161, -0.0706), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK = Template(
    filename=r"DORM_NAV_KITCHEN_TASK_ASSIGN_CLICK.png", 
    record_pos=(0.4005, 0.2414), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键派遣'),
    rgb=False, 
    template_path="assets/dorm",
)