import time
import math

class Timer:
    def __init__(self, timeout_sec: float = 10, auto_start=False):
        """
        初始化计时器
        :param timeout_sec: 超时时间（秒）
        :param auto_start: 是否自动开始计时（默认False）
        """
        self.timeout_sec = timeout_sec
        self.start_time = None
        self._is_stopped = False
        if auto_start:
            self.start()

    def start(self):
        """开始/重启计时（清空之前的状态）"""
        self.start_time = time.time()
        self._is_stopped = False

    def stop(self):
        """停止计时（is_timeout()将永远返回False）"""
        self._is_stopped = True

    def reset(self):
        """清空计时（回到初始状态，需重新调用start()才能使用）"""
        self.start_time = None
        self._is_stopped = False

    def is_timeout(self) -> bool:
        """检查是否超时（已停止或未启动的计时器返回False）"""
        if self._is_stopped or self.start_time is None:
            return False
        return (time.time() - self.start_time) >= self.timeout_sec

    def remaining_time(self) -> float:
        """返回剩余时间（秒），未启动返回inf，已停止返回nan"""
        if self.start_time is None:
            return math.inf
        if self._is_stopped:
            return math.nan
        elapsed = time.time() - self.start_time
        return max(0.0, self.timeout_sec - elapsed)

    def elapsed_time(self) -> float:
        """返回已计时时间（秒），未启动返回nan"""
        if self.start_time is None:
            return math.nan
        return time.time() - self.start_time

    def show_info(self) -> None:
        remain_time = self.remaining_time()
        if remain_time == math.inf or remain_time == math.nan:
            raise ValueError("计时器未启动或已停止")
        print(f"任务总计用时: {remain_time:.1f}秒")

# ---------- 使用示例 ----------
if __name__ == "__main__":
    timer = Timer(timeout_sec=3)
    
    print(f"初始状态 - 剩余时间: {timer.remaining_time()}")  # inf（未启动）
    
    timer.start()
    time.sleep(1)
    print(f"启动后 - 剩余时间: {timer.remaining_time():.1f}秒")  # 2.0秒
    
    timer.stop()
    print(f"停止后 - 是否超时: {timer.is_timeout()}")          # False
    print(f"停止后 - 剩余时间: {timer.remaining_time()}")      # nan
    
    timer.reset()
    print(f"清空后 - 剩余时间: {timer.remaining_time()}")      # inf（回到初始状态）