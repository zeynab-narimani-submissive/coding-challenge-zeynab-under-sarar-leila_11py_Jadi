def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper
@do_twice
def print_role():
    print("I am submissive to miss Leila and miss Sara")

print_role()
