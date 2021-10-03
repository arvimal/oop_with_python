#!/usr/bin/env python


def decorator(inner):
    def inner_decorator(*args, **kwargs):
        print("This function takes " + str(len(args)) + " arguments")
        inner(*args)

    return inner_decorator


@decorator
def decorated(string_args):
    print("This happened: " + str(string_args))


@decorator
def alsoDecorated(num1, num2):
    print("Sum of " + str(num1) + "and" + str(num2) + ": " + str(num1 + num2))


if __name__ == "__main__":
    decorated("Hello")
    alsoDecorated(1, 2)
