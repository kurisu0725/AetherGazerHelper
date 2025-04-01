import cv2
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QRect, QSize, pyqtSignal, QPoint

class ImageLabel(QLabel):
    mouseReleaseSignal = pyqtSignal(QRect)
    
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("border: 2px solid black;")
        self.setMinimumSize(100, 100)
        
        self.original_pixmap = None
        self.display_pixmap = None
        self.drawing = False
        self.selection_rect = QRect()
        self.start_point = None
        self.scale_factor = 1.0
        self.offset = QPoint(0, 0)
    
    def display_image(self, cv_image):
        """显示OpenCV图像并计算缩放参数"""
        if cv_image is None:
            self.clear()
            return
            
        # 转换OpenCV图像为QImage
        if len(cv_image.shape) == 2:
            q_img = QImage(cv_image.data, 
                         cv_image.shape[1], 
                         cv_image.shape[0], 
                         QImage.Format_Grayscale8)
        else:
            rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            q_img = QImage(rgb.data, 
                         rgb.shape[1], 
                         rgb.shape[0], 
                         rgb.strides[0], 
                         QImage.Format_RGB888)
        
        self.original_pixmap = QPixmap.fromImage(q_img)
        self.update_display()
    
    def update_display(self):
        """更新显示（考虑缩放）"""
        if self.original_pixmap is None:
            return
            
        # 计算缩放后的尺寸
        scaled_size = self.original_pixmap.size()
        scaled_size.scale(self.size(), Qt.KeepAspectRatio)
        
        # 计算缩放因子和偏移量
        self.scale_factor = min(
            scaled_size.width() / self.original_pixmap.width(),
            scaled_size.height() / self.original_pixmap.height()
        )
        self.offset = QPoint(
            (self.width() - scaled_size.width()) // 2,
            (self.height() - scaled_size.height()) // 2
        )
        
        # 创建显示用的pixmap
        self.display_pixmap = self.original_pixmap.scaled(
            scaled_size, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        
        # 绘制图像和选择框
        final_pixmap = QPixmap(self.size())
        final_pixmap.fill(Qt.white)
        
        painter = QPainter(final_pixmap)
        painter.drawPixmap(self.offset, self.display_pixmap)
        
        # 绘制选择框
        if self.drawing and not self.selection_rect.isEmpty():
            pen = QPen(Qt.green, 2, Qt.DashLine)
            painter.setPen(pen)
            
            # 将图像坐标转换为显示坐标
            display_rect = QRect(
                int(self.selection_rect.x() * self.scale_factor) + self.offset.x(),
                int(self.selection_rect.y() * self.scale_factor) + self.offset.y(),
                int(self.selection_rect.width() * self.scale_factor),
                int(self.selection_rect.height() * self.scale_factor)
            )
            painter.drawRect(display_rect)
        
        painter.end()
        self.setPixmap(final_pixmap)
    
    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if self.original_pixmap is not None and event.button() == Qt.LeftButton:
            self.drawing = True
            # 将点击位置转换为原始图像坐标
            img_pos = self.window_to_image_pos(event.pos())
            self.start_point = QPoint(img_pos.x(), img_pos.y())
            self.selection_rect = QRect(self.start_point, QSize())
            self.update_display()
    
    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        if self.drawing and self.original_pixmap is not None:
            # 将当前位置转换为原始图像坐标
            img_pos = self.window_to_image_pos(event.pos())
            # 更新选择矩形
            self.selection_rect = QRect(
                self.start_point,
                QPoint(img_pos.x(), img_pos.y())
            ).normalized()
            self.update_display()
    
    def mouseReleaseEvent(self, event):
        """鼠标释放事件"""
        if self.drawing:
            self.drawing = False
            if (self.selection_rect.width() >= 5 and self.selection_rect.height() >= 5):
                # 确保发射的是有效的QRect
                roi = QRect(self.selection_rect)
                print("roi:", roi)
                if roi.isValid():
                    print("roi valid.....")
                    self.mouseReleaseSignal.emit(roi)
            else:
                print("roi width or height too short.")
            self.selection_rect = QRect()
            self.update_display()
        super().mouseReleaseEvent(event)

    def window_to_image_pos(self, pos):
        """将窗口坐标转换为原始图像坐标"""
        if not self.original_pixmap or not self.display_pixmap:
            return QPoint(0, 0)
            
        # 计算相对于显示图像的坐标
        x = pos.x() - self.offset.x()
        y = pos.y() - self.offset.y()
        
        # 转换为原始图像坐标
        img_x = int(x / self.scale_factor)
        img_y = int(y / self.scale_factor)
        
        # 确保坐标在图像范围内
        img_x = max(0, min(img_x, self.original_pixmap.width() - 1))
        img_y = max(0, min(img_y, self.original_pixmap.height() - 1))
        
        return QPoint(img_x, img_y)
    
    def resizeEvent(self, event):
        """窗口大小改变事件"""
        super().resizeEvent(event)
        self.update_display()