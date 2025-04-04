from zafkiel import Template
from zafkiel.ocr import Keyword

MAIN_TO_STAMINA = Template(
    filename=r"MAIN_TO_STAMINA.png",
    record_pos=(0.0974, -0.2536), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/daily",
)

DAILY_STAMINA_CLAIM_AM = Template(
    filename=r"DAILY_STAMINA_CLAIM_AM.png",
    record_pos=(0.0573, 0.1062), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/daily",
)

DAILY_STAMINA_CLAIM_PM = Template(
    filename=r"DAILY_STAMINA_CLAIM_PM.png",
    record_pos=(0.2552, 0.1078), 
    resolution=(1920, 1080) , 
    rgb=True, 
    template_path="assets/daily",
)