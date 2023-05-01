def greeting(func):
    def inner(*args, **kwargs):
        print("Hello")
        func(*args, **kwargs)
        print("Nice to meet you!")
    return inner


@greeting
def say_name(name):
    print(f"I'm {name}")


@greeting
def say_name_origin(name, origin):
    print(f"I'm {name} ,I'm from {origin}")


# say_name("kazu")
say_name_origin("kazu", "nagano")
