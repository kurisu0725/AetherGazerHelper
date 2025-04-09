from zafkiel import Template
from zafkiel.ocr import Keyword

POPUP_ACTIVITY_CHECK = Template(
    filename=r"POPUP_ACTIVITY_CHECK.png",
    record_pos=(0.27, 0.19), 
    keyword=Keyword(u'今日登录不再提示'),
    resolution=(1600, 900) , 
    rgb=False, 
    template_path="assets/share/base/popup",
)

POPUP_ACTIVITY_CLICK = Template(
    filename=r"POPUP_ACTIVITY_CLICK.png",
    record_pos=(0.00, 0.24), 
    keyword=Keyword(u'点击图片进行跳转'),
    resolution=(1600, 900) , 
    rgb=False, 
    template_path="assets/share/base/popup",
)

POPUP_CHECK_IN_REWARD_CHECK = Template(
    filename=r"POPUP_CHECK_IN_REWARD_CHECK.png",
    record_pos=(-0.36, -0.18), 
    keyword=Keyword(u'每日签到'),
    resolution=(1600, 900) , 
    rgb=False, 
    template_path="assets/share/base/popup",
)

POPUP_BATTLE_PASS_CHECK = Template(
    filename=r"POPUP_BATTLE_PASS_CHECK.png",
    record_pos=(-0.2698, 0.1247), 
    resolution=(1920, 1080), 
    rgb=True, 
    template_path="assets/share/base/popup",
)