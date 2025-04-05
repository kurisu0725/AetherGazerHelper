from zafkiel import Template
from tasks.base.assets.assets_switch import *
from zafkiel.ui import Switch

switch_mission = Switch('switch_mission', is_selector=True)
switch_mission.add_state('MISSION_DAILY_SWITCH_ON', MISSION_DAILY_SWITCH_ON, MISSION_DAILY_SWITCH_OFF)
switch_mission.add_state('MISSION_WEEKLY_SWITCH_ON', MISSION_WEEKLY_SWITCH_ON, MISSION_WEEKLY_SWITCH_OFF)