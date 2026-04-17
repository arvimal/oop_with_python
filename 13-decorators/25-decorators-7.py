#!/usr/bin/env python

# 25-decorators-7.py

# Reference https://www.youtube.com/watch?v=Slf1b3yUocc

# We have two functions, one which adds two numbers,
# and another which subtracts two numbers.

# We apply the decorator @double which takes in the
# functions that is called with the decorator, and doubles
# the output of the respective function.


def double(my_func):
    def inner_func(a, b):
        return 2 * my_func(a, b)

    return inner_func


@double
def adder(a, b):
    return a + b


@double
def subtractor(a, b):
    return a - b


print(adder(10, 20))
print(subtractor(6, 1))
