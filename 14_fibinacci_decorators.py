import time

def my_decorator(func):
    def wrapper(n):
        print("شروع")
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"پایان - زمان اجرا: {end_time - start_time} ثانیه")
        return result
    return wrapper

@my_decorator
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for n in range(10):
    print(fib(n), end=" ")