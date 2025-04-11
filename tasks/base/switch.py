from zafkiel import Template
from tasks.base.assets.assets_switch import *
from zafkiel.ui import Switch

switch_mission = Switch('switch_mission', is_selector=True)
switch_mission.add_state('MISSION_DAILY_SWITCH_ON', MISSION_DAILY_SWITCH_ON, MISSION_DAILY_SWITCH_OFF)
switch_mission.add_state('MISSION_WEEKLY_SWITCH_ON', MISSION_WEEKLY_SWITCH_ON, MISSION_WEEKLY_SWITCH_OFF)

switch_resource = Switch('switch_resource', is_selector=True)
switch_resource.add_state('RESOURCE_INFORMATION_SWITCH_ON', RESOURCE_INFORMATION_SWITCH_ON, RESOURCE_INFORMATION_SWITCH_OFF)
switch_resource.add_state('RESOURCE_ITEMS_SWITCH_ON', RESOURCE_ITEMS_SWITCH_ON, RESOURCE_ITEMS_SWITCH_OFF)
switch_resource.add_state('RESOURCE_SIGILS_SWITCH_ON', RESOURCE_SIGILS_SWITCH_ON, RESOURCE_SIGILS_SWITCH_OFF)
switch_resource.add_state('RESOURCE_CHALLENGE_SWITCH_ON', RESOURCE_CHALLENGE_SWITCH_ON, RESOURCE_CHALLENGE_SWITCH_OFF)