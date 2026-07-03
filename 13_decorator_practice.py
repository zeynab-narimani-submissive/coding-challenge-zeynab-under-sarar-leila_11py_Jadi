def my_decorator(func):
    def wrapper(a, b):
        print("شروع")
        func(a,b)
        print("پایان")
    return wrapper
@my_decorator
def sumuel(a,b):
    print(a + b)
sumuel(80, 5)