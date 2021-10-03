#!/usr/bin/env python

# Reference: Decorators 101 - A Gentle Introduction to Functional Programming.
# By Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc

# This is an updated version of 20-decorators-2.py.
# Here, the `decorated()` function takes an argument
# and prints it back on terminal.

# When the decorator `@my_decorator` is called, it
# takes the function `decorated()` as its argument, and
# the argument of `decorated()` as the argument of `inner_decorator()`.
# Hence the arg `number` is passed to `num_copy`.

import datetime


def my_decorator(inner):
    def inner_decorator(num_copy):
        print(datetime.datetime.utcnow())
        inner(int(num_copy) + 1)
        print(datetime.datetime.utcnow())

    return inner_decorator


@my_decorator
def decorated(number):
    print("This happened : " + str(number))


if __name__ == "__main__":
    decorated(5)

# This prints:
# python 21-decorators-3.py
# 2016-05-29 12:11:57.212125
# This happened : 6
# 2016-05-29 12:11:57.212168
