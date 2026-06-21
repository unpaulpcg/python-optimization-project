import time
from functools import wraps

def timer_decorator(func):
    """실행 시간을 측정하는 데코레이터"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{end_time:.4f}] '{func.__name__}' 실행 완료 | 소요 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper