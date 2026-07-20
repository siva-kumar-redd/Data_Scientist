def decorator(func):

    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("Finish")

    return wrapper


@decorator
def employee(name, salary):
    print(name)
    print(salary)

employee(name="Rahul", salary=50000)