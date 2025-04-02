from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton, QLineEdit, QFileDialog)
from PyQt5.QtCore import pyqtSignal
from views.image_label import ImageLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):

        # 主窗口设置
        self.setWindowTitle("Image Cropper")
        self.setGeometry(100, 100, 1200, 800)
        
        # 主部件和布局
        central_widget = QWidget()
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        
        # 图像显示区域
        self.original_label = ImageLabel("Original Image")
        self.cropped_label = ImageLabel("Cropped Image")
        left_layout.addWidget(self.original_label, 70)
        left_layout.addWidget(self.cropped_label, 30)
        
        # 控制区域
        self.load_btn = QPushButton("Load Image")
        self.save_btn = QPushButton("Save Cropped Image")
        self.save_btn.setEnabled(False)
        
        # ROI信息显示
        self.roi_info_label = QLabel("ROI (normalized to width):")
        self.roi_x_label = QLabel("x: ")
        self.roi_y_label = QLabel("y: ")
        self.roi_w_label = QLabel("width: ")
        self.roi_h_label = QLabel("height: ")
        self.roi_rel_y_label = QLabel("relative y: ")     # 新增：y按width归一化
        self.roi_rel_x_label = QLabel("relative x: ")     

        # 保存路径设置
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("Select save directory...")
        self.browse_btn = QPushButton("Browse")
        
        # 文件名设置
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter file name (without extension)")
        
        # 添加到右侧布局
        right_layout.addWidget(self.load_btn)
        right_layout.addWidget(self.save_btn)
        right_layout.addSpacing(20)
        right_layout.addWidget(self.roi_info_label)
        right_layout.addWidget(self.roi_x_label)
        right_layout.addWidget(self.roi_y_label)
        right_layout.addWidget(self.roi_w_label)
        right_layout.addWidget(self.roi_h_label)
        right_layout.addWidget(self.roi_rel_x_label)
        right_layout.addWidget(self.roi_rel_y_label)  # 新增：y按高度归一化
       
        right_layout.addSpacing(20)
        right_layout.addWidget(QLabel("Save Path:"))
        right_layout.addWidget(self.path_edit)
        right_layout.addWidget(self.browse_btn)
        right_layout.addWidget(QLabel("File Name:"))
        right_layout.addWidget(self.name_edit)
        right_layout.addStretch()
        
        # 合并布局
        main_layout.addLayout(left_layout, 70)
        main_layout.addLayout(right_layout, 30)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def get_image_path(self):
        """获取图像路径"""
        path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", 
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tif)"
        )
        return path
    
    def get_save_path(self):
        """获取保存路径"""
        return self.path_edit.text()
    
    def get_file_name(self):
        """获取文件名"""
        return self.name_edit.text()
    
    def display_original_image(self, image):
        """显示原始图像"""
        self.original_label.display_image(image)


    def update_roi_info(self, orig_roi, norm_roi, relative_x, relative_y):
        """更新ROI信息显示"""
        self.roi_x_label.setText(f"x: {orig_roi[0]:.1f} -> {norm_roi[0]:.4f}")
        self.roi_rel_x_label.setText(f"relative x: {relative_x:.4f}")
        self.roi_y_label.setText(f"y: {orig_roi[1]:.1f} -> {norm_roi[1]:.4f}")
        self.roi_rel_y_label.setText(f"relative y: {relative_y:.4f}")  # 新增：y按高度归一化
        self.roi_w_label.setText(f"width: {orig_roi[2]:.1f} -> {norm_roi[2]:.4f}")
        self.roi_h_label.setText(f"height: {orig_roi[3]:.1f} -> {norm_roi[3]:.4f}")
        self.roi_info_label.setVisible(True)

    def display_cropped_image(self, image):
        """显示裁剪后的图像"""
        if image is not None:
            self.cropped_label.display_image(image)
            self.save_btn.setEnabled(True)
        else:
            self.cropped_label.clear()
            self.save_btn.setEnabled(False)
