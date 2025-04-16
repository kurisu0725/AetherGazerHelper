from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import QRect, QEvent
import cv2
import os
import logging
class MainController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view
        self.connect_signals()
    
    def connect_signals(self):
        """连接所有信号"""
        self.view.load_btn.clicked.connect(self.btn_load_image)
        self.view.save_btn.clicked.connect(self.save_image)
        self.view.browse_btn.clicked.connect(self.browse_directory)

        # 图像crop的触发信号
        self.view.original_label.mouseReleaseSignal.connect(self.handle_roi_selection)
        # 拖拽图像文件输入的信号
        self.view.original_label.imageDropped.connect(self.handle_image_drop)

        # 窗口缩放信号（通过事件过滤器实现）
        self.view.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        """处理窗口缩放"""
        if obj == self.view and event.type() == QEvent.Resize:
            self.handle_resize(event)
        return super().eventFilter(obj, event)

    def handle_resize(self, event):
        """处理窗口缩放事件"""
        self.view.original_label.update_display()
        self.view.cropped_label.update_display()
        event.accept()
    
    def handle_image_drop(self, file_path):
        """处理拖拽的图像文件"""
        logging.info(f"handle image drop -> file path : {file_path}")
        success = self.load_image(file_path)
        if success:
            logging.info("Image loaded successfully!")
        else:
            QMessageBox.warning(self.view, "Error", "Failed to load the image!")

    def handle_roi_selection(self, rect):
        """处理ROI选择"""
        print(f"handle_roi_selection -> ROI selected: {rect}")
        try:
            if not isinstance(rect, QRect) or not rect.isValid():
                return
            print(f"ROI selected: {rect}")
            # 获取ROI参数
            x, y, w, h = rect.x(), rect.y(), rect.width(), rect.height()
            orig_roi = (x, y, w, h)
            # 执行裁剪
            norm_roi = self.model.crop_image(orig_roi)

            relative_x, relative_y = self.model.recalculate_xy()
            print(f"norm_roi: {norm_roi}, relative_x: {relative_x}, relative_y: {relative_y}")
            if norm_roi is not None and self.model.cropped_image is not None:
                # 显示裁剪结果
                self.view.display_cropped_image(self.model.cropped_image)
                
                # 更新ROI信息
                self.view.update_roi_info(orig_roi, norm_roi, relative_x, relative_y)
                
                # 启用保存按钮
                self.view.save_btn.setEnabled(True)
        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"裁剪失败: {str(e)}")

    def load_image(self, path) -> bool:
        if path is None:
            return False
        success = self.model.load_image(path)
        if not success:
            return False
        self.view.display_original_image(self.model.original_image)
        # 自动填充文件名
        base_name = os.path.splitext(os.path.basename(path))[0]
        self.view.name_edit.setText(base_name)
        self.view.path_edit.setText(os.path.dirname(path))
        return True

    def btn_load_image(self):
        """处理图像加载"""
        path = self.view.get_image_path()
        self.load_image(path)
    
    def browse_directory(self):
        """处理目录选择"""
        directory = QFileDialog.getExistingDirectory(self.view, "Select Save Directory")
        if directory:
            self.view.path_edit.setText(directory)
    
    def save_image(self):
        """处理图像保存"""
        if self.model.cropped_image is None or self.model.cropped_image.size == 0:
            QMessageBox.warning(self.view, "Error", "No cropped image to save!")
            return
            
        save_dir = self.view.get_save_path()
        if not save_dir:
            QMessageBox.warning(self.view, "Error", "Please select a save directory!")
            return
            
        file_name = self.view.get_file_name()
        file_name = file_name.upper()
        if not file_name:
            QMessageBox.warning(self.view, "Error", "Please enter a file name!")
            return
            
        try:
            # 保存图像
            img_path = save_dir
            os.makedirs(img_path, exist_ok=True)
            img_name = f"{file_name}.png"
            cv2.imwrite(os.path.join(img_path, img_name), self.model.cropped_image)
            
            # 保存ROI信息
            roi_path = os.path.join(img_path, f"{file_name}_roi.txt")
            norm_roi = self.model.norm_roi
            relative_x, relative_y = self.model.relative_x, self.model.relative_y

            with open(roi_path, 'w') as f:
                f.write(f"Normalized ROI (x, y, width, height):\n")
                f.write(f"x: {norm_roi[0]:.4f}\n")
                f.write(f"y: {norm_roi[1]:.4f}\n")
                f.write(f"width: {norm_roi[2]:.4f}\n")
                f.write(f"height: {norm_roi[3]:.4f}\n")
                f.write(f"Template record pos: ({relative_x:.4f}, {relative_y:.4f})\n")
            
            QMessageBox.information(
                self.view, "Success", 
                f"Image and ROI saved successfully!\n\n"
                f"Image: {img_path}\n"
                f"ROI info: {roi_path}"
            )
        except Exception as e:
            QMessageBox.critical(self.view, "Error", f"Failed to save files:\n{str(e)}")