import cv2
import numpy as np
import logging

class ImageModel:
    def __init__(self):
        self.original_image = None
        self.cropped_image = None
        self.norm_roi = None  # (x, y, w, h)
        self.orig_roi = None
        self.relative_x : float = None
        self.relative_y : float = None
        self.rect_center_x : float = None
        self.rect_center_y : float = None
    
    def load_image(self, path):
        self.original_image = cv2.imread(path)
        self.cropped_image = None
        self.norm_roi = None
        self.orig_roi = None
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
        self.orig_roi = roi
        self.norm_roi = self.get_normalized_roi()
        self.rect_center_x = x + w / 2
        self.rect_center_y = y + h / 2
        return self.norm_roi

    def get_normalized_roi(self):
        """
        返回归一化的ROI信息 (x_w, y_h, w_w, h_h)
        :param img_width: 原始图像宽度
        :return: 包含4个归一化值的元组
        """
        if self.original_image is None:
            print("original image is None")
            return None
            
        x, y, w, h = self.orig_roi
        img_height, img_width = self.original_image.shape[:2]
        
        return (
            x / img_width,        # x按宽度归一化
            y / img_height,        # y按高度归一化
            w / img_width,        # width归一化
            h / img_height,        # height归一化
        )

    def recalculate_xy(self):
        """
        重新计算ROI的x和y坐标
        x, y 以图像中心点为(0, 0) , 以宽度为基准，适配自动化的Template 
        """
        if self.relative_x is not None and self.relative_y is not None:
            return self.relative_x, self.relative_y
        if self.original_image is None:
            return None
        total_height, total_width = self.original_image.shape[:2]
        half_height, half_width = total_height / 2, total_width / 2

        self.relative_x = (self.rect_center_x - half_width) / total_width
        self.relative_y = (self.rect_center_y - half_height) / total_width # 以宽度为基准，适配自动化的Template
        
        return self.relative_x, self.relative_y