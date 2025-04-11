from zafkiel import Template
from zafkiel.ocr import Keyword

MAIN_TO_STAMINA = Template(
    filename=r"MAIN_TO_STAMINA.png",
    record_pos=(0.0974, -0.2536), 
    resolution=(1920, 1080) , 
    rgb=False, 
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



ACTIVITY_SEARCH_BUTTON = Template(
    filename=r"ACTIVITY_SEARCH_BUTTON.png",
    record_pos=(-0.3870, -0.0005), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/daily",
)

ACTIVITY_SWIPE_START = Template(
    filename=r"ACTIVITY_SWIPE_START.png",
    record_pos=(-0.3971, -0.0336), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/daily",
)

RESOURCE_SEARCH_BUTTON = Template(
    filename=r"RESOURCE_SEARCH_BUTTON.png",
    record_pos=(0.0000, 0.1651), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/daily",
)

RESOURCE_NEXT_BUTTON = Template(
    filename=r"RESOURCE_NEXT_BUTTON.png",
    record_pos=(0.1552, 0.1487), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/daily",
)

RESOURCE_PREV_BUTTON = Template(
    filename=r"RESOURCE_NEXT_BUTTON.png",
    record_pos=(-0.1536, 0.1492), 
    resolution=(1920, 1080) , 
    rgb=False, 
    template_path="assets/daily",
)