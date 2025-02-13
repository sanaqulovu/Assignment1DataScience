import time
import contextlib

def decorator_1(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        with contextlib.redirect_stdout(None):
            f(*args, **kwargs)
        end = time.time()
        print(f"{f.__name__} call executed in {end - start : .7f} sec")
    return wrapper
