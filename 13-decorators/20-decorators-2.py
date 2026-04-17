#!/usr/bin/env python

# Reference: Decorators 101 - A Gentle Introduction to Functional Programming.
# By Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc

# 20-decorators-2.py
# An updated version of 19-decorators-1.py

# This code snippet takes the previous example, and add a bit more information
# to the output.

import datetime


def my_decorator(inner):
    def inner_decorator():
        print(datetime.datetime.utcnow())
        inner()
        print(datetime.datetime.utcnow())

    return inner_decorator


@my_decorator
def decorated():
    print("This happened!")


if __name__ == "__main__":
    decorated()

# This will print: (NOTE: The time will change of course :P)
# # python 20-decorators-2.py
# 2016-05-29 11:46:07.444330
# This happened!
# 2016-05-29 11:46:07.444367
