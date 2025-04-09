import inspect
import datetime

def get_current_weekday_and_time(language='en'):
    """
    获取当前星期几和时间
    :param language: 输出语言，'en' 英文 | 'zh' 中文
    :return: (weekday, time_str) 
    """
    now = datetime.datetime.now()
    
    # 获取星期几（数字 0-6，0=周一或周日，根据系统设置）
    weekday_num = now.weekday()  # Python中0=周一，6=周日
    
     # 星期几映射表
    weekday_map = {
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'zh': ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    }
    
    # 获取时间字符串
    time_str = now.strftime('%H:%M:%S')
    
    print(f"Today is {weekday_map[language][weekday_num]}, current time is {time_str}")
    # 返回结果
    return weekday_num, time_str