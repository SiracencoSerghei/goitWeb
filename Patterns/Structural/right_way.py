import time
from functools import wraps


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper

@wrong_timelogger
def long_wrong_loop(num: int) -> None:
    """
    Long wrong loop function

    :param num:
    :return: None
    """

    while num > 0:
        num -= 1


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper


@timelogger
def long_loop(num: int) -> None:
    """
    Long loop function

    :param num:
    :return: None
    """

    while num > 0:
        num -= 1


if __name__ == '__main__':
    
    long_wrong_loop(100_000)
    print(long_wrong_loop.__name__)
    print(long_wrong_loop.__doc__)
    print(long_wrong_loop.__annotations__)
    print("=================")
    long_loop(100_000)
    print(long_loop.__name__)
    print(long_loop.__doc__)
    print(long_loop.__annotations__)
