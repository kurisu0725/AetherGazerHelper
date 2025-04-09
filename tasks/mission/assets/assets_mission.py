from zafkiel import Template
from zafkiel.ocr import Keyword

MISSION_DAILY_CLAIM = Template(
    filename=r"MISSION_DAILY_CLAIM.png", 
    record_pos=(0.4102, 0.2391), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键领取'),
    rgb=True, 
    template_path="assets/mission",
)

MISSION_WEEKLY_CLAIM = Template(
    filename=r"MISSION_DAILY_CLAIM.png", 
    record_pos=(0.4102, 0.2391), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键领取'),
    rgb=False, 
    template_path="assets/mission",
)

BATTLE_PASS_CLAIM_ALL_CLICK = Template(
    filename=r"BATTLE_PASS_CLAIM_ALL_CLICK.png", 
    record_pos=(0.4099, 0.2437), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键领取'),
    rgb=False, 
    template_path="assets/mission",
)

BATTLE_PASS_MISSION_CLAIM_ALL_CLICK = Template(
    filename=r"BATTLE_PASS_CLAIM_ALL_CLICK.png", 
    record_pos=(0.4099, 0.2437), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键领取'),
    rgb=False, 
    template_path="assets/mission",
)