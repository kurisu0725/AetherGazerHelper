import cv2
import numpy as np

class ImageModel:
    def __init__(self):
        self.original_image = None
        self.cropped_image = None
        self.roi = None  # (x, y, w, h)
    
    def load_image(self, path):
        self.original_image = cv2.imread(path)
        self.cropped_image = None
        self.roi = None
        return self.original_image is not None
    
    def crop_image(self, roi):
        """执行裁剪并返回归一化ROI"""
        if self.original_image is None:
            return None
            
        x, y, w, h = roi
        img_h, img_w = self.original_image.shape[:2]
        
        # 确保ROI在图像范围内
        x = max(0, min(x, img_w - 1))
        y = max(0, min(y, img_h - 1))
        w = max(1, min(w, img_w - x))
        h = max(1, min(h, img_h - y))
        
        self.cropped_image = self.original_image[y:y+h, x:x+w]
        self.roi = (x, y, w, h)
        
        # 返回归一化ROI (相对于宽度)
        return (x/img_w, y/img_h, w/img_w, h/img_h)

    def get_normalized_roi(self, img_width):
        """
        返回归一化的ROI信息 (x_w, y_h, w_w, h_h)
        :param img_width: 原始图像宽度
        :return: 包含4个归一化值的元组
        """
        if self.roi is None or img_width == 0:
            return None
            
        x, y, w, h = self.roi
        img_height = self.original_image.shape[0]
        
        return (
            x / img_width,        # x按宽度归一化
            y / img_height,        # y按高度归一化
            w / img_width,        # width按宽度归一化
            h / img_height,        # height归一化
        )