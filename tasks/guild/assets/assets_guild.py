from zafkiel import Template
from zafkiel.ocr import Keyword

GUILD_MATRIX_SUPPLY = Template(
    filename=r"GUILD_MATRIX_SUPPLY.png",
    record_pos=(0.380, 0.245), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_MATRIX_SUPPLY_CLAIM = Template(
    filename=r"GUILD_MATRIX_SUPPLY_CLAIM.png",
    record_pos=(-0.0005, 0.118), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_MATRIX_SUPPLY_COMPLETE = Template(
    filename=r"GUILD_MATRIX_SUPPLY_COMPLETE.png",
    record_pos=(0.000, 0.118), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_MISSION_CLAIM_CLICK = Template(
    filename=r"GUILD_MISSION_CLAIM_CLICK.png",
    record_pos=(0.4284, -0.1494), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_TO_GUILD_MISSION = Template(
    filename=r"GUILD_TO_GUILD_MISSION.png",
    record_pos=(0.2560, 0.2451), 
    resolution=(1920, 1080), 
    rgb=False, 
    template_path="assets/guild",
)

GUILD_STORE_SIGIL_MODULE_T3 = Template(
    filename=r"GUILD_STORE_SIGIL_MODULE_T3.png",
    record_pos=(-0.2385, -0.0956), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_STORE_SIGIL_CORE = Template(
    filename=r"GUILD_STORE_SIGIL_CORE.png",
    record_pos=(-0.0779, -0.0951), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_STORE_PURCHASE_PLUS = Template(
    filename=r"GUILD_STORE_PURCHASE_PLUS.png",
    record_pos=(0.1620, 0.1089), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/guild",
)

GUILD_STORE_PURCHASE_NUMBER = Template(
    filename=r"GUILD_STORE_PURCHASE_NUMBER.png",
    record_pos=(0.0667, 0.0893), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/guild",
)

GUILD_STORE_PURCHASE_LIMIT_NUMBER = Template(
    filename=r"GUILD_STORE_PURCHASE_LIMIT_NUMBER.png",
    record_pos=(0.0516, 0.1286), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/guild",
)

GUILD_STORE_PURCHASE_CLICK = Template(
    filename=r"GUILD_STORE_PURCHASE_CLICK.png",
    record_pos=(0.2719, 0.1091), 
    resolution=(1920, 1080) , 
    keyword=Keyword(u'购买'),
    rgb=False, 
    template_path="assets/guild",
)

GUILD_TO_GUILD_STORE = Template(
    filename=r"GUILD_TO_GUILD_STORE.png",
    record_pos=(0.1753, 0.2445), 
    resolution=(1920, 1080), 
    keyword=Keyword(u'矩阵供应'),
    rgb=False, 
    template_path="assets/guild",
)