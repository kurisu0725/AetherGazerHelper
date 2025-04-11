import cv2
from zafkiel import Template

def match_template(image, template, similarity=0.85):
    """
    from StarRailCopilot/module/base/button.py
    Args:
        image (np.ndarray): Screenshot
        template (np.ndarray):
        area (tuple): Crop area of image.
        offset (int, tuple): Detection area offset.
        similarity (float): 0-1. Similarity. Lower than this value will return float(0).

    Returns:
        bool:
    """
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, sim, _, point = cv2.minMaxLoc(res)
    return sim > similarity

