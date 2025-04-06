from zafkiel import Template
from zafkiel.ocr import Keyword

MAIL_REWARD_CLICK = Template(
    filename=r"MAIL_REWARD_CLICK.png",
    record_pos=(-0.3195, 0.1859), 
    resolution=(1920, 1080), 
    keyword=Keyword(u'全部领取'),
    rgb=False, 
    template_path="assets/mail",
)