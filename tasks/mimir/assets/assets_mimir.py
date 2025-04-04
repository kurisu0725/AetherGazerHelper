from zafkiel import Template
from zafkiel.ocr import Keyword

MIMI_OBSERVATION_CLAIM_ALL = Template(
    filename=r"MIMI_OBSERVATION_CLAIM_ALL.png",
    record_pos=(0.253, 0.223), 
    resolution=(1920, 1080) , 
    keyword=Keyword(u'一键领取'),
    rgb=False, 
    template_path="assets/mimir",
)

MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK = Template(
    filename=r"MIMI_OBSERVATION_EXPLORATION_COMPLETE_CHECK.png",
    record_pos=(0.000, -0.155), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/mimir",
)

MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK = Template(
    filename=r"MIMI_OBSERVATION_EXPLORATION_COMPLETE_CLICK.png",
    record_pos=(0.000, 0.139), 
    resolution=(1920, 1080), 
    rgb=True, 
    template_path="assets/mimir",
)

MIMI_OBSERVATION_DISPATCH = Template(
    filename=r"MIMI_OBSERVATION_DISPATCH.png",
    record_pos=(0.25, 0.222), 
    resolution=(1920, 1080), 
    keyword=Keyword(u'一键派遣'),
    template_path="assets/mimir",
)