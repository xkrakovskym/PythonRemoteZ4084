import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the func")

        result = func(*args, **kwargs)

        print("After calling func")

        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello {name}!")


say_hello("Michal")
