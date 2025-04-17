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

TO_TRAIN = Template(
    filename=r"TO_TRAIN.png", 
    record_pos=(-0.1771, 0.2482), 
    resolution=(1920, 1080),
    keyword=Keyword(u'修正者'),
    rgb=False, 
    template_path="assets/dorm",    
)

TRAIN_SEARCH_BUTTON = Template(
    filename=r"TRAIN_SEARCH_BUTTON.png", 
    record_pos=(-0.4221, 0.0201), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/dorm",
)

TRAIN_SKIP_ANIMATION = Template(
    filename=r"TRAIN_SKIP_ANIMATION.png", 
    record_pos=(-0.0112, 0.2289), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/dorm",
)

OCR_TRAIN_MODIFIER_STAMINA = Template(
    filename=r"OCR_TRAIN_MODIFIER_STAMINA.png", 
    record_pos=(-0.2357, 0.1836), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

OCR_TRAIN_COUNT = Template(
    filename=r"OCR_TRAIN_COUNT.png", 
    record_pos=(0.2089, -0.1971), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_1 = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_1.png", 
    record_pos=(0.1245, 0.2460), 
    resolution=(1920, 1080),
    keyword=Keyword('20'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_2 = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_2.png", 
    record_pos=(0.2049, 0.2461), 
    resolution=(1920, 1080),
    keyword=Keyword('20'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_3 = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_3.png", 
    record_pos=(0.2862, 0.2461), 
    resolution=(1920, 1080),
    keyword=Keyword('20'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_4 = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_4.png", 
    record_pos=(0.3648, 0.2466), 
    resolution=(1920, 1080),
    keyword=Keyword('20'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_5 = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_5.png", 
    record_pos=(0.4461, 0.2471), 
    resolution=(1920, 1080),
    keyword=Keyword('20'),
    rgb=False, 
    template_path="assets/dorm",
)


TRAIN_MODIFIER_ABILITY_1_CLICK = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_1_CLICK.png", 
    record_pos=(0.1177, 0.2161), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_2_CLICK = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_2_CLICK.png", 
    record_pos=(0.1979, 0.2174), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_3_CLICK = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_3_CLICK.png", 
    record_pos=(0.2781, 0.2159), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_4_CLICK = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_4_CLICK.png", 
    record_pos=(0.3583, 0.2161), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MODIFIER_ABILITY_5_CLICK = Template(
    filename=r"TRAIN_MODIFIER_ABILITY_5_CLICK.png", 
    record_pos=(0.4388, 0.2148), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/dorm",
)

TO_TRAIN_MISSION = Template(
    filename=r"TO_TRAIN_MISSION.png", 
    record_pos=(-0.3135, 0.2477), 
    resolution=(1920, 1080),
    keyword=Keyword(u'任务'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MISSION_CLAIM_CLICK = Template(
    filename=r"TRAIN_MISSION_CLAIM_CLICK.png", 
    record_pos=(0.2232, 0.1940), 
    resolution=(1920, 1080),
    keyword=Keyword(u'一键领取'),
    rgb=False, 
    template_path="assets/dorm",
)

TRAIN_MISSION_CLAIM_CHECK = Template(
    filename=r"TRAIN_MISSION_CLAIM_CHECK.png", 
    record_pos=(-0.2456, -0.2018), 
    resolution=(1920, 1080),
    keyword=Keyword(u'阶段目标'),
    rgb=False, 
    template_path="assets/dorm",
)

TO_MODIFIER_COMBAT = Template(
    filename=r"TO_MODIFIER_COMBAT.png", 
    record_pos=(0.4073, 0.2284), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/dorm",
)


MODIFIER_COMBAT_CLICK = Template(
    filename=r"MODIFIER_COMBAT_CLICK.png", 
    record_pos=(0.2901, 0.2229), 
    resolution=(1920, 1080),
    keyword=Keyword(u'玩家挑战'),
    rgb=True, 
    template_path="assets/dorm",
)

MODIFIER_COMBAT_SELECT_STRANGER = Template(
    filename=r"MODIFIER_COMBAT_SELECT_STRANGER.png", 
    record_pos=(-0.3982, -0.1951), 
    resolution=(1920, 1080),
    keyword=Keyword(u'陌生人'),
    rgb=False, 
    template_path="assets/dorm",
)

MODIFIER_COMBAT_SELECT_TO_CHALLENGE = Template(
    filename=r"MODIFIER_COMBAT_SELECT_TO_CHALLENGE.png", 
    record_pos=(0.0013, -0.1341), 
    resolution=(1920, 1080),
    keyword=Keyword(u'挑战'),
    rgb=False, 
    template_path="assets/dorm",
)

KITCHEN_DISPATCH_CONFIRM_CHECK = Template(
    filename=r"KITCHEN_DISPATCH_CONFIRM_CHECK.png",
    record_pos=(-0.1104, -0.0784),
    resolution=(1920, 1080),
    rgb=False,
    template_path="assets/dorm",
)

KITCHEN_DISPATCH_CONFIRM_CLICK = Template(
    filename=r"KITCHEN_DISPATCH_CONFIRM_CLICK.png",
    record_pos=(0.0008, 0.2331),
    resolution=(1920, 1080),
    keyword=Keyword(u'确定'),
    rgb=False,
    template_path="assets/dorm",
)

MODIFIER_COMBATTING_CHECK = Template(
    filename=r"MODIFIER_COMBATTING_CHECK.png",
    record_pos=(0.0031, 0.1893),
    resolution=(1920, 1080),
    rgb=True,
    template_path="assets/dorm",
)

MODIFIER_COMBAT_END_AGAIN = Template(
    filename=r"MODIFIER_COMBAT_END_AGAIN.png",
    record_pos=(-0.1081, 0.1953),
    resolution=(1920, 1080),
    keyword=Keyword(u'再次挑战'),
    rgb=False,
    template_path="assets/dorm",
)

MODIFIER_COMBAT_END_CHECK = Template(
    filename=r"MODIFIER_COMBAT_END_CHECK.png",
    record_pos=(-0.0013, -0.1026),
    resolution=(1920, 1080),
    keyword=Keyword(u'回顾'),
    rgb=False,
    template_path="assets/dorm",
)

MODIFIER_COMBAT_END_CLICK = Template(
    filename=r"MODIFIER_COMBAT_END_CLICK.png",
    record_pos=(0.1047, 0.1969),
    resolution=(1920, 1080),
    keyword=Keyword(u'返回'),
    rgb=False,
    template_path="assets/dorm",
)