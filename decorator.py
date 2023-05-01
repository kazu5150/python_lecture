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
    print(f"I'm {name}. ,I'm from {origin}")


@greeting
def say_name_dob_origin(name, origin, dob):
    print(f"I'm {name}. I'm from {origin}. I was born in {dob}.")


# say_name("kazu")
# say_name_origin("kazu", "nagano")
say_name_dob_origin("kazu", "nagano", "1963/12/19")
