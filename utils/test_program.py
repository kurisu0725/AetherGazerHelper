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
    """以管理员权限重新启动脚本"""
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        sys.exit()