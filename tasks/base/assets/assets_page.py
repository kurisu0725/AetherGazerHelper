from zafkiel import Template
from zafkiel.ocr import Keyword

MAIN_CHECK = Template(
    filename=r"MAIN_TO_MAIL.png", 
    record_pos=(0.3586, -0.2172), 
    resolution=(1920, 1080),
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
    record_pos=(0.4128, -0.2159), 
    resolution=(1920, 1080),
    rgb = False,
    template_path="assets/share/base/page",
)

MIMIR_CHECK = Template(
    filename=r"MIMIR_TO_MIMI_OBSERVATION.png", 
    record_pos=(0.3339, -0.0456), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/share/base/page",
)


MIMIR_TO_MIMI_OBSERVATION = Template(
    filename=r"MIMIR_TO_MIMI_OBSERVATION.png", 
    record_pos=(0.3339, -0.0456), 
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


MAIN_TO_MISSION = Template(
    filename=r"MAIN_TO_MISSION.png", 
    record_pos=(0.3177, -0.2169), 
    resolution=(1920, 1080),
    rgb=True,
    template_path="assets/share/base/page",
)

MISSION_CHECK = Template(
    filename=r"MISSION_CHECK.png", 
    record_pos=(-0.3945, -0.1883), 
    resolution=(1920, 1080),
    keyword=Keyword(u'每日任务'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_STORE = Template(
    filename=r"MAIN_TO_STORE.png", 
    record_pos=(0.0677, 0.2531), 
    resolution=(1920, 1080),
    keyword=Keyword(u'商店'),
    rgb=False, 
    template_path="assets/share/base/page",
)

STORE_CHECK = Template(
    filename=r"STORE_CHECK.png", 
    record_pos=(-0.185, 0.207), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)

STORE_TO_STORE_SUPPLY = Template(
    filename=r"STORE_CHECK.png", 
    record_pos=(-0.1862, 0.1991), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)


STORE_SUPPLY_CHECK = Template(
    filename=r"STORE_SUPPLY_CHECK.png", 
    record_pos=(-0.4006, 0.2441), 
    resolution=(1920, 1080),
    keyword=Keyword(u'累计充值'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_MAIL = Template(
    filename=r"MAIN_TO_MAIL.png", 
    record_pos=(0.3586, -0.2172), 
    resolution=(1920, 1080),
    rgb=False,
    template_path="assets/share/base/page",
)

MAIL_CHECK = Template(
    filename=r"MAIL_CHECK.png", 
    record_pos=(-0.4391, -0.1977), 
    resolution=(1920, 1080),
    keyword=Keyword(u'邮件'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_DORM = Template(
    filename=r"MAIN_TO_DORM.png", 
    record_pos=(0.2867, 0.2526), 
    resolution=(1920, 1080),
    keyword=Keyword(u'游园街'),
    rgb=False,
    template_path="assets/share/base/page",
)

DORM_CHECK = Template(
    filename=r"DORM_CHECK.png", 
    record_pos=(0.2156, 0.2385), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)

DORM_NAV_CHECK = Template(
    filename=r"DORM_NAV_CHECK.png", 
    record_pos=(0.0026, -0.0135), 
    resolution=(1920, 1080),
    keyword=Keyword(u'宿舍'),
    rgb=False, 
    template_path="assets/share/base/page",
)


DORM_NAV_KITCHEN_CHECK = Template(
    filename=r"DORM_NAV_KITCHEN_CHECK.png", 
    record_pos=(0.0003, -0.2589), 
    resolution=(1920, 1080),
    keyword=Keyword(u'餐厅'),
    rgb=False, 
    template_path="assets/share/base/page",
)


DORM_TO_DORM_NAV = Template(
    filename=r"DORM_TO_DORM_NAV.png", 
    record_pos=(-0.3992, 0.2456), 
    resolution=(1920, 1080),
    keyword=Keyword(u'导航'),
    rgb=False, 
    template_path="assets/share/base/page",
)

DORM_NAV_TO_DORM_NAV_CHARACTER = Template(
    filename=r"DORM_NAV_TO_DORM_NAV_CHARACTER.png", 
    record_pos=(0.1906, 0.1031), 
    resolution=(1920, 1080),
    keyword=Keyword(u'训练室'),
    rgb=False, 
    template_path="assets/share/base/page",
)

DORM_NAV_TO_DORM_NAV_KITCHEN = Template(
    filename=r"DORM_NAV_TO_DORM_NAV_KITCHEN.png", 
    record_pos=(-0.2375, 0.0664), 
    resolution=(1920, 1080),
    keyword=Keyword(u'餐厅'),
    rgb=False, 
    template_path="assets/share/base/page",
)

DORM_NAV_KITCHEN_TO_DORM_NAV = Template(
    filename=r"DORM_TO_DORM_NAV.png", 
    record_pos=(-0.3992, 0.2456), 
    resolution=(1920, 1080),
    keyword=Keyword(u'导航'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_BATTLE_PASS = Template(
    filename=r"MAIN_TO_BATTLE_PASS.png", 
    record_pos=(-0.4586, -0.1607), 
    resolution=(1920, 1080),
    keyword=Keyword(u'对策协议'),
    rgb=False, 
    template_path="assets/share/base/page",
)

BATTLE_PASS_CHECK = Template(
    filename=r"BATTLE_PASS_CHECK.png", 
    record_pos=(-0.2008, -0.1073), 
    resolution=(1920, 1080),
    keyword=Keyword(u'基础合约'),
    rgb=False, 
    template_path="assets/share/base/page",
)

DORM_NAV_CHARACTER_CHECK = Template(
    filename=r"DORM_NAV_CHARACTER_CHECK.png", 
    record_pos=(-0.1771, 0.2276), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)

BATTLE_PASS_TO_BATTLE_PASS_MISSION = Template(
    filename=r"BATTLE_PASS_TO_BATTLE_PASS_MISSION.png", 
    record_pos=(-0.3977, 0.2422), 
    resolution=(1920, 1080),
    keyword=Keyword(u'任务'),
    rgb=False, 
    template_path="assets/share/base/page",
)

BATTLE_PASS_MISSION_CHECK = Template(
    filename=r"BATTLE_PASS_MISSION_CHECK.png", 
    record_pos=(-0.3883, -0.1896), 
    resolution=(1920, 1080),
    keyword=Keyword(u'今日任务'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_ACTIVITY = Template(
    filename=r"MAIN_TO_ACTIVITY.png", 
    record_pos=(0.3917, -0.1198), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)

ACTIVITY_CHECK = Template(
    filename=r"ACTIVITY_CHECK.png", 
    record_pos=(-0.4536, 0.2513), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)


RESOURCE_CHECK = Template(
    filename=r"RESOURCE_CHECK.png", 
    record_pos=(-0.3641, 0.2375), 
    resolution=(1920, 1080),
    rgb=True, 
    template_path="assets/share/base/page",
)

MAIN_TO_RESOURCE = Template(
    filename=r"MAIN_TO_RESOURCE.png", 
    record_pos=(0.4151, 0.2466), 
    resolution=(1920, 1080),
    rgb=False, 
    template_path="assets/share/base/page",
)