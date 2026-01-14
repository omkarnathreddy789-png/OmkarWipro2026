import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function Name:", func.__name__)
        print("Execution Time:", end - start)
        return result
    return wrapper
