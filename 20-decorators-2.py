#!/usr/bin/env python

# Reference: Decorators 101 - A Gentle Introduction to Functional Programming.
# By Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc


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
