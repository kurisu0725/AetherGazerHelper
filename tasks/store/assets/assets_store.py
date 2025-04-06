from zafkiel import Template
from zafkiel.ocr import Keyword

STORE_SUPPLY_DAILY_SUPPLY_CLICK = Template(
    filename=r"STORE_SUPPLY_DAILY_SUPPLY_CLICK.png",
    record_pos=(-0.0891, -0.1919),
    resolution=(1920, 1080),
    keyword=Keyword(u'日常补给'),
    rgb=False,
    template_path="assets/store",
)

STORE_SUPPLY_FREE_STAMINA_CHECK = Template(
    filename=r"STORE_SUPPLY_FREE_STAMINA_CHECK.png",
    record_pos=(-0.2029, -0.0828),
    resolution=(1920, 1080),
    rgb=False,
    threshold=0.7,
    template_path="assets/store",
)

STORE_SUPPLY_FREE_STAMINA_CLICK = Template(
    filename=r"STORE_SUPPLY_FREE_STAMINA_CLICK.png",
    record_pos=(-0.2034, 0.0284),
    resolution=(1920, 1080),
    keyword=Keyword(u'免费'),
    rgb=False,
    template_path="assets/store",
)

STORE_SUPPLY_PURCHASE_CHECK = Template(
    filename=r"STORE_SUPPLY_PURCHASE_CHECK.png",
    record_pos=(-0.1516, -0.0987),
    resolution=(1920, 1080),
    rgb=True,
    threshold=0.7,
    template_path="assets/store",
)

STORE_SUPPLY_PURCHASE_CLICK = Template(
    filename=r"STORE_SUPPLY_PURCHASE_CLICK.png",
    record_pos=(0.1953, 0.1966),
    resolution=(1920, 1080),
    keyword=Keyword(u'确定'),
    rgb=False,
    template_path="assets/store",
)