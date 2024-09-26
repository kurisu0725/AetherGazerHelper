from pywinauto import Application

app = Application().connect(class_name="Internet Explorer_Hidden")
# 查找该应用的所有窗口
windows = app.windows()
print(windows)  # 打印所有窗口以查看其属性
