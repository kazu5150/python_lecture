def my_decorator(func):
    def wrapper():
        print("Hi, there!")
        func()
    return wrapper


@my_decorator
def hello_world():
    print("Hello, World!")


hello_world()
