def do_twice(func):
    func
    func
    return func
@do_twice
def print_role():
    print("I am submissive to miss Leila and miss Sara")

print(do_twice(print_role()))