from zafkiel import Template
from zafkiel.ocr import Keyword

MISSION_DAILY_SWITCH_ON = Template(
    filename="MISSION_DAILY_SWITCH_ON.png",
    record_pos=(-0.455, -0.188),
    resolution=(1920, 1080),
    rgb=True,
    threshold=0.8,
    template_path="assets/base/switch",
)

MISSION_DAILY_SWITCH_OFF = Template(
    filename="MISSION_DAILY_SWITCH_OFF.png",
    record_pos=(-0.455, -0.188),
    resolution=(1920, 1080),
    rgb=True,
    threshold=0.8,
    template_path="assets/base/switch",
)

MISSION_WEEKLY_SWITCH_ON = Template(
    filename="MISSION_WEEKLY_SWITCH_ON.png",
    record_pos=(-0.455, -0.126),
    resolution=(1920, 1080),
    rgb=True,
    threshold=0.8,
    template_path="assets/base/switch",
)

MISSION_WEEKLY_SWITCH_OFF = Template(
    filename="MISSION_WEEKLY_SWITCH_OFF.png",
    record_pos=(-0.455, -0.126),
    resolution=(1920, 1080),
    rgb=True,
    threshold=0.8,
    template_path="assets/base/switch",
)
