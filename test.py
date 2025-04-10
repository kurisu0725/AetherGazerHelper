import cv2
import time
import numpy as np

def gpu_template_matching(image, template):
    # 上传数据到GPU
    gpu_image = cv2.cuda_GpuMat()
    gpu_template = cv2.cuda_GpuMat()
    gpu_image.upload(image)
    gpu_template.upload(template)
    
    # 创建CUDA模板匹配器
    matcher = cv2.cuda.createTemplateMatching(cv2.CV_8UC1, cv2.TM_CCOEFF_NORMED)
    
    # 执行匹配
    result = matcher.match(gpu_image, gpu_template)
    
    # 下载结果到CPU
    return result.download()

# def torch_template_matching(image, template):
#     # 转换为PyTorch张量并上传到GPU
#     image_tensor = torch.from_numpy(image).float().unsqueeze(0).unsqueeze(0).cuda()
#     template_tensor = torch.from_numpy(template).float().unsqueeze(0).unsqueeze(0).cuda()
    
#     # 使用卷积操作实现模板匹配
#     result = F.conv2d(image_tensor, template_tensor)
    
#     # 返回结果
#     return result.squeeze().cpu().numpy()

if __name__ == "__main__":
    # 读取图像和模板
    image = cv2.imread('main.png', cv2.IMREAD_GRAYSCALE)
    template = cv2.imread('Main_Flag.png', cv2.IMREAD_GRAYSCALE)

    # CPU版本
    start = time.time()
    cpu_result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    print(f"CPU耗时: {time.time()-start:.3f}s")

    # GPU版本
    # start = time.time()
    # gpu_result = gpu_template_matching(image, template)
    # print(f"GPU耗时: {time.time()-start:.3f}s")

    # torch 
    # start = time.time()
    # torch_result = torch_template_matching(image, template)
    # print(f"Torch耗时: {time.time()-start:.3f}s")
