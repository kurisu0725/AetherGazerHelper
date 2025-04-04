from zafkiel import Template
from zafkiel.ocr import Keyword

MAIN_CHECK = Template(
    filename=r"MAIN_CHECK.png", 
    record_pos=(-0.07, 0.25), 
    resolution=(1600, 900),
    keyword=Keyword(u'修正者'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_STORE = Template(
    filename=r"MAIN_TO_STORE.png", 
    record_pos=(0.06, 0.25), 
    resolution=(1600, 900),
    keyword=Keyword(u'商店'),
    rgb=False, 
    template_path="assets/share/base/page",
)

GUILD_CHECK = Template(
    filename=r"GUILD_CHECK.png", 
    record_pos=(-0.40, -0.19), 
    resolution=(1920, 1080),
    keyword=Keyword(u'矩阵公会'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_GUILD = Template(
    filename=r"MAIN_TO_GUILD.png", 
    record_pos=(0.14, 0.25), 
    resolution=(1920, 1080),
    keyword=Keyword(u'公会'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_MIMIR = Template(
    filename=r"MAIN_TO_MIMIR.png", 
    record_pos=(0.41, -0.21), 
    resolution=(1920, 1080),
    template_path="assets/share/base/page",
)

MIMIR_CHECK = Template(
    filename=r"MIMIR_TO_MIMI_OBSERVATION.png", 
    record_pos=(0.33, -0.04), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/share/base/page",
)


MIMIR_TO_MIMI_OBSERVATION = Template(
    filename=r"MIMIR_TO_MIMI_OBSERVATION.png", 
    record_pos=(0.33, -0.04), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/share/base/page",
)

MIMI_OBSERVATION_CHECK = Template(
    filename=r"MIMI_OBSERVATION_CHECK.png", 
    record_pos=(-0.437, 0.150), 
    resolution=(1920, 1080),
    keyword=Keyword(u'探索等级'),
    rgb=False, 
    template_path="assets/share/base/page",
)