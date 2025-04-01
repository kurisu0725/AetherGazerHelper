import sys
import cv2
import numpy as np
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QFileDialog,
                             QLineEdit, QSpinBox, QMessageBox)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QRect, QMimeData
from PyQt5.Qt import QDragEnterEvent, QDropEvent

class ImageCropper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Cropper Tool")
        self.setGeometry(100, 100, 1200, 800)
        
        # 初始化变量
        self.original_image = None
        self.cropped_image = None
        self.drawing = False
        self.roi = QRect()
        self.start_point = None
        # 启用拖放
        self.setAcceptDrops(True)

        # 创建UI
        self.init_ui()
        

    def init_ui(self):
        # 主窗口部件
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # 布局
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        
        # 左侧面板 - 图像显示
        self.original_label = QLabel("Original Image")
        self.original_label.setAlignment(Qt.AlignCenter)
        self.original_label.setStyleSheet("border: 2px solid black;")
        self.original_label.mousePressEvent = self.mouse_press
        self.original_label.mouseMoveEvent = self.mouse_move
        self.original_label.mouseReleaseEvent = self.mouse_release
        
        self.cropped_label = QLabel("Cropped Image")
        self.cropped_label.setAlignment(Qt.AlignCenter)
        self.cropped_label.setStyleSheet("border: 2px solid black;")
        
        left_layout.addWidget(self.original_label, 70)
        left_layout.addWidget(self.cropped_label, 30)
        
        # 右侧面板 - 控制区
        self.load_btn = QPushButton("Load Image")
        self.load_btn.clicked.connect(self.load_image)
        
        self.save_btn = QPushButton("Save Cropped Image")
        self.save_btn.clicked.connect(self.save_image)
        self.save_btn.setEnabled(False)
        
        # ROI信息显示
        self.roi_info_label = QLabel("ROI (normalized to width):")
        self.roi_x_label = QLabel("x: ")
        self.roi_y_label = QLabel("y: ")
        self.roi_w_label = QLabel("width: ")
        self.roi_h_label = QLabel("height: ")
        
        # 保存路径和文件名
        self.path_label = QLabel("Save Path:")
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText("Select save directory...")
        self.browse_btn = QPushButton("Browse")
        self.browse_btn.clicked.connect(self.browse_directory)
        
        self.name_label = QLabel("File Name:")
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
        right_layout.addSpacing(20)
        right_layout.addWidget(self.path_label)
        right_layout.addWidget(self.path_edit)
        right_layout.addWidget(self.browse_btn)
        right_layout.addWidget(self.name_label)
        right_layout.addWidget(self.name_edit)
        right_layout.addStretch()
        
        # 合并布局
        main_layout.addLayout(left_layout, 70)
        main_layout.addLayout(right_layout, 30)
        main_widget.setLayout(main_layout)
    
    # --- 新增拖放支持的核心方法 ---
    def dragEnterEvent(self, event: QDragEnterEvent):
        """检查拖入的文件是否为图像"""
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and urls[0].toLocalFile().lower().endswith(
                ('.png', '.jpg', '.jpeg', '.bmp', '.tif')
            ):
                event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        """处理拖放的图像文件"""
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.load_image_from_path(file_path)

    def load_image(self):
        """通过按钮加载图像（调用拖放的相同方法）"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", 
            "Image Files (*.png *.jpg *.jpeg *.bmp *.tif)"
        )
        if file_path:
            self.load_image_from_path(file_path)
    
    def load_image_from_path(self, file_path):
        """从路径加载图像（供拖放和普通加载共用）"""
        if os.path.exists(file_path):
            self.original_image = cv2.imread(file_path)
            if self.original_image is not None:
                self.display_image(self.original_image, self.original_label)
                self.save_btn.setEnabled(True)
                self.cropped_label.clear()
                self.clear_roi_info()
                # 自动填充文件名（不含扩展名）
                base_name = os.path.splitext(os.path.basename(file_path))[0]
                self.name_edit.setText(base_name)
            else:
                QMessageBox.warning(self, "Error", "Failed to load image!")
        else:
            QMessageBox.warning(self, "Error", "File not exists!")

    def display_image(self, image, label):
        """在QLabel上显示OpenCV图像"""
        if len(image.shape) == 2:  # 灰度图
            q_img = QImage(
                image.data, 
                image.shape[1], 
                image.shape[0], 
                QImage.Format_Grayscale8
            )
        else:  # 彩色图
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            q_img = QImage(
                rgb_image.data, 
                rgb_image.shape[1], 
                rgb_image.shape[0], 
                rgb_image.strides[0], 
                QImage.Format_RGB888
            )
        
        pixmap = QPixmap.fromImage(q_img)
        label.setPixmap(
            pixmap.scaled(
                label.width(), 
                label.height(), 
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )
    
    def mouse_press(self, event):
        """鼠标按下事件 - 开始选择ROI"""
        if self.original_image is None:
            return
            
        self.drawing = True
        self.start_point = event.pos()
        self.roi = QRect(self.start_point, self.start_point)
    
    def mouse_move(self, event):
        """鼠标移动事件 - 更新ROI"""
        if self.drawing and self.original_image is not None:
            self.roi = QRect(
                self.start_point, 
                event.pos()
            ).normalized()
            
            # 在图像上绘制矩形
            temp_image = self.original_image.copy()
            cv2.rectangle(
                temp_image,
                (self.roi.x(), self.roi.y()),
                (self.roi.x() + self.roi.width(), self.roi.y() + self.roi.height()),
                (0, 255, 0),
                2
            )
            self.display_image(temp_image, self.original_label)
    
    def mouse_release(self, event):
        """鼠标释放事件 - 完成ROI选择并裁剪"""
        if self.drawing and self.original_image is not None:
            self.drawing = False
            
            # 确保ROI在图像范围内
            img_height, img_width = self.original_image.shape[:2]
            x = max(0, min(self.roi.x(), img_width - 1))
            y = max(0, min(self.roi.y(), img_height - 1))
            w = max(1, min(self.roi.width(), img_width - x))
            h = max(1, min(self.roi.height(), img_height - y))
            
            self.roi = QRect(x, y, w, h)
            
            # 裁剪图像
            self.cropped_image = self.original_image[y:y+h, x:x+w]
            self.display_image(self.cropped_image, self.cropped_label)
            
            # 计算并显示归一化ROI
            self.update_roi_info(img_width)
    
    def update_roi_info(self, img_width):
        """更新ROI信息（归一化到宽度）"""
        if img_width == 0:
            return
            
        norm_x = self.roi.x() / img_width
        norm_y = self.roi.y() / img_width  # 注意：这里y也除以宽度
        norm_w = self.roi.width() / img_width
        norm_h = self.roi.height() / img_width
        
        self.roi_x_label.setText(f"x: {norm_x:.4f}")
        self.roi_y_label.setText(f"y: {norm_y:.4f}")
        self.roi_w_label.setText(f"width: {norm_w:.4f}")
        self.roi_h_label.setText(f"height: {norm_h:.4f}")
    
    def clear_roi_info(self):
        """清除ROI信息"""
        self.roi_x_label.setText("x: ")
        self.roi_y_label.setText("y: ")
        self.roi_w_label.setText("width: ")
        self.roi_h_label.setText("height: ")
    
    def browse_directory(self):
        """选择保存目录"""
        directory = QFileDialog.getExistingDirectory(
            self, "Select Save Directory"
        )
        if directory:
            self.path_edit.setText(directory)
    
    def save_image(self):
        """保存裁剪后的图像和ROI信息"""
        if self.cropped_image is None:
            QMessageBox.warning(self, "Error", "No cropped image to save!")
            return
            
        save_dir = self.path_edit.text()
        if not save_dir:
            QMessageBox.warning(self, "Error", "Please select a save directory!")
            return
            
        file_name = self.name_edit.text()
        if not file_name:
            QMessageBox.warning(self, "Error", "Please enter a file name!")
            return
            
        # 保存图像
        try:
            img_path = f"{save_dir}/{file_name}.png"
            cv2.imwrite(img_path, self.cropped_image)
            
            # 保存ROI信息
            roi_path = f"{save_dir}/{file_name}_roi.txt"
            with open(roi_path, 'w') as f:
                f.write(f"Normalized ROI (x, y, width, height):\n")
                f.write(f"{self.roi_x_label.text()}\n")
                f.write(f"{self.roi_y_label.text()}\n")
                f.write(f"{self.roi_w_label.text()}\n")
                f.write(f"{self.roi_h_label.text()}\n")
            
            QMessageBox.information(
                self, "Success", 
                f"Image and ROI saved successfully!\n\n"
                f"Image: {img_path}\n"
                f"ROI info: {roi_path}"
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Error", 
                f"Failed to save files:\n{str(e)}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageCropper()
    window.show()
    sys.exit(app.exec_())