from typing import Dict
from zafkiel import Template, logger, Timer
from zafkiel.ui import UI, Page
from zafkiel.ocr import DigitCounter
from zafkiel.exception import LoopError
from tasks.base.assets.assets_switch import *
from tasks.dispatch_room.assets.assets_dispatch_room import *

class DispatchRoom(UI):
    
    def __init__(self, config: Dict = None):
        self.config = config

    def dispatch(self):
        """
        进入调度室派遣队伍
        Example path: 调度室 -> 领取派遣奖励 -> 再次派遣
        """
        pass
    def claim_rewards(self):
        """
        调度收益：领取情报储备（体力），和资源生产（日常资源）
        """
        logger.info('Start claim rewards')
        self.ui_ensure(page_dispatch_reward)

        # 选择 情报储备选项
        self.ui_goto(page_dispatch_reward, state=DISPATCH_REWARD_INTELLIGENCE_RESERVE_SWITCH_ON)

        ocr = DigitCounter(DISPATCH_REWARD_INTELLIGENCE_RESERVE_VALUE)
        is_exceed = ocr.ocr_single_line(self.screenshot())[0]
        logger.info(f"Ocr value: {is_exceed}")
        if is_exceed > 0:
            # 若没有选中 "最大" 按钮
            if self.exists(DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_OFF):
                self.touch(DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_OFF)
                logger.info("Choose 'Max' Button")
            if self.exists(DISPATCH_REWARD_INTELLIGENCE_RESERVE_MAX_ON):
                self.find_click(DISPATCH_REWARD_INTELLIGENCE_RESERVE_TAKE_OUT)
                logger.info(f"Take out {is_exceed} INTELLIGENCE_RESERVE")

        
    def run(self):
        logger.info(f"Start DispatchRoom process")
        logger.info(f"{Page.all_pages}")
        # 确认当前是否在调度室，若不在该界面则调用ui_goto
        self.ui_ensure(page_dispatch_room)
        self.dispatch()
        self.claim_rewards()