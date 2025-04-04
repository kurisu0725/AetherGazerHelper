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