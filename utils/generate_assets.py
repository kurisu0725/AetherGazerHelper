import cv2
import os

# 全局变量
start_point = None
end_point = None
drawing = False
clone = None

# 鼠标回调函数
def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        drawing = False
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Image", image)

def save_selected_area(image, start, end, filename):
    x1, y1 = start
    x2, y2 = end
    rect = image[y1:y2, x1:x2]
    cv2.imwrite(f"../templates/{filename}.png", rect)
    print(f"Selected area saved as 'templates/{filename}.png'.")

def calculate_relative_position(start, end, image_shape):
    # 计算图像中心
    h, w = image_shape[:2]
    center_x, center_y = w / 2, h / 2

    # 计算选中矩形的中心
    rect_center_x = (start[0] + end[0]) / 2
    rect_center_y = (start[1] + end[1]) / 2

    # 计算相对位置
    relative_x = (rect_center_x - center_x) / w
    relative_y = (rect_center_y - center_y) / w

    return relative_x, relative_y

# 保存assets_task.py文件
# def save_assets_task(variable_name, task_name, x, y):
    
#     file_path = f"../tasks/{task_name}/assets_{task_name}.py"
#     is_new_file = not os.path.exists(file_path)
    
#     with open(file_path, "a") as f:  # 使用 "a" 模式追加内容
#         if is_new_file:
#             f.write(f"from zafkiel import Template\n\n")  # 只在新文件时写入import
#         f.write(f"{variable_name} = Template(r\"{image_path}\", ({x}, {y}))\n")
    
#     print(f"{variable_name} generated in {file_path}.")

if __name__ == "__main__":
    # 读取图片
    image_path = "../screenshot/dispatch_reward_max_off.png"
    image = cv2.imread(image_path)
    clone = image.copy()

    print(f"image shape: {image.shape}")

    # 创建窗口并设置鼠标回调
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_rectangle)
    
    while True:
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF

        # 按 's' 键保存选定区域
        if key == ord("s") and start_point and end_point:
            save_selected_area(clone, start_point, end_point, filename='DISPATCH_REWARD_INTELLIGENCE_RESERVE_TAKE_OUT'.upper())
            relative_position = calculate_relative_position(start_point, end_point, image.shape)
            print(f"Relative position: (x: {relative_position[0]}, y: {relative_position[1]})")

        # 按 'q' 键退出
        elif key == ord("q"):
            break

    cv2.destroyAllWindows()
    