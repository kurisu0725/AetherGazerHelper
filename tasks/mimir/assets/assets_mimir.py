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

MIMI_OBSERVATION_WEEKLY_REWARD = Template(
    filename=r"MIMI_OBSERVATION_WEEKLY_REWARD.png",
    record_pos=(0.4076, 0.2224), 
    resolution=(1920, 1080), 
    keyword=Keyword(u'堆栈递归'),
    template_path="assets/mimir",
)

MIMI_OBSERVATION_WEEKLY_REWARD_OPEN = Template(
    filename=r"MIMI_OBSERVATION_WEEKLY_REWARD_OPEN.png",
    record_pos=(0.2335, -0.0005), 
    resolution=(1920, 1080), 
    template_path="assets/mimir",
)

MIMI_OBSERVATION_WEEKLY_REWARD_CLAIM = Template(
    filename=r"MIMI_OBSERVATION_WEEKLY_REWARD_CLAIM.png",
    record_pos=(0.0026, -0.0013), 
    resolution=(1920, 1080), 
    template_path="assets/mimir",
)