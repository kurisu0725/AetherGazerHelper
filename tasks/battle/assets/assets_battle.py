from zafkiel import Template
from zafkiel.ocr import Keyword

STAMINA_COST = Template(
    filename=r"STAMINA_COST.png",
    record_pos=(0.3708, 0.2057), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/battle",
)

STAGE_SWEEP = Template(
    filename=r"STAGE_SWEEP.png",
    record_pos=(0.2831, 0.2440), 
    resolution=(1920, 1080) , 
    keyword=Keyword(u"扫荡"),
    rgb=True, 
    template_path="assets/battle",
)

RIGHT_DOUBLE_ARROW = Template(
    filename=r"RIGHT_DOUBLE_ARROW.png",
    record_pos=(0.4596, 0.1659), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/battle",
)

RIGHT_ARROW = Template(
    filename=r"RIGHT_ARROW.png",
    record_pos=(0.4284, 0.1648), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/battle",
)

REMAIN_STAMINA = Template(
    filename=r"REMAIN_STAMINA.png",
    record_pos=(0.1789, -0.2544), 
    resolution=(1920, 1080), 
    rgb=False, 
    template_path="assets/battle",
)

SWEEP_END_CHECK = Template(
    filename=r"SWEEP_END_CHECK.png",
    record_pos=(-0.4081, -0.2583), 
    resolution=(1920, 1080), 
    keyword=Keyword(u"扫荡完成"),
    rgb=False, 
    template_path="assets/battle",
)

SWEEP_END_CLICK = Template(
    filename=r"SWEEP_END_CLICK.png",
    record_pos=(0.4125, 0.2401), 
    resolution=(1920, 1080), 
    keyword=Keyword(u"确认"),
    rgb=False, 
    template_path="assets/battle",
)

SWEEP_CONFIRM_CHECK = Template(
    filename=r"SWEEP_CONFIRM_CHECK.png",
    record_pos=(-0.0013, -0.1471), 
    resolution=(1920, 1080), 
    keyword=Keyword(u"快速扫荡"),
    rgb=False, 
    template_path="assets/battle",
)

SWEEP_CONFIRM_CLICK = Template(
    filename=r"SWEEP_CONFIRM_CLICK.png",
    record_pos=(0.1958, 0.1966), 
    resolution=(1920, 1080), 
    keyword=Keyword(u"确认"),
    rgb=False, 
    template_path="assets/battle",
)