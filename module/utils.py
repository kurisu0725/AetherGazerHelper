import cv2
import numpy as np
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

def stitch_image(img1, img2):
    stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)  # 或使用 cv2.createStitcher()（旧版本）
    status, result = stitcher.stitch([img1, img2])

    if status == cv2.Stitcher_OK:
        return result
    else:
        print(f"拼接失败，错误码: {status}")

def hough_circle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. 高斯模糊降噪（减少边缘噪声）
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # 3. 霍夫圆检测
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, 
        dp=1,            # 累加器分辨率
        minDist=50,      # 圆之间的最小距离
        param1=80,      # Canny 高阈值
        param2=30,       # 累加器阈值（越小检测越多圆）
        minRadius=50,    # 最小半径
        maxRadius=150    # 最大半径
    )

    # 4. 绘制检测到的圆
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (x, y, r) in circles[0, :]:
            # 绘制圆
            cv2.circle(image, (x, y), r, (0, 255, 0), 2)
            # 绘制圆心
            cv2.circle(image, (x, y), 2, (0, 0, 255), 3)

    # 5. 显示结果
    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img1 = cv2.imread(r"D:\VSCode_Workplace\Python\GF2_Exilium_Script\tmp_imgs\train_1.png")
    # img2 = cv2.imread(r"D:\VSCode_Workplace\Python\GF2_Exilium_Script\tmp_imgs\train_2.png")
    x, y = 70, 131
    w, h = 151, 896
    img1 = img1[y:y+h, x:x+w]
    # img2 = img2[y:y+h, x:x+w]
    # stitched_img = stitch_image(img1, img2)
    cv2.imwrite('crop_img1.png', img1)
    hough_circle(img1)

    # cv2.imwrite('crop_img2.png', img2)
    # cv2.imwrite('stitched_image.png', stitched_img)