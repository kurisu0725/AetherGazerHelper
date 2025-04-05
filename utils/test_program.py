import os
import sys
import datetime
from pathlib import Path
import ctypes
import datetime

def is_admin():
    """检查是否以管理员权限运行"""
    try:
        return os.getuid() == 0  # Unix 系统
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin()  # Windows

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, 
            ' '.join([f'"{arg}"' for arg in sys.argv]), None, 1
        )
        sys.exit()

def test_task():
    run_as_admin()
    from pathlib import Path
    import datetime
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    process_str = "少女前线2：追放"
    
    # team.auto_setup(str(Path.cwd()), logdir=f'./log/{date}/report', devices=[f"WindowsPlatform:///?title={process_str}", ])
    # team.take_supply()