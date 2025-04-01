import sys
from PyQt5.QtWidgets import QApplication
from models.image_model import ImageModel
from views.main_window import MainWindow
from controllers.main_controller import MainController

def main():
    app = QApplication(sys.argv)
    
    # 初始化MVC
    model = ImageModel()
    view = MainWindow()
    controller = MainController(model, view)
    
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()