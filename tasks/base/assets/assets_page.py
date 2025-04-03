from zafkiel import Template
from zafkiel.ocr import Keyword

MAIN_CHECK = Template(filename=r"MAIN_CHECK.png", 
    record_pos=(-0.07, 0.25), 
    resolution=(1600, 900),
    keyword=Keyword(u'修正者'),
    rgb=False, 
    template_path="assets/share/base/page",
)

MAIN_TO_STORE = Template(
    filename=r"MAIN_TO_STORE.png", 
    record_pos=(0.06, 0.25), 
    resolution=(1600, 900),
    keyword=Keyword(u'商店'),
    rgb=False, 
    template_path="assets/share/base/page",
)