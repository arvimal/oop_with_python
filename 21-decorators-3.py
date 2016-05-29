#!/usr/bin/env python

# Reference: Decorators 101 - A Gentle Introduction to Functional Programming.
# By Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc

import datetime


def decorator(inner):
    def inner_decorator(num_copy):
    	print(datetime.datetime.utcnow())
    	inner(int(num_copy) + 1)
    	print(datetime.datetime.utcnow())
    return inner_decorator

@decorator
def decorated(number):
	print("This happened : " + str(number))

if __name__ == "__main__":
	decorated(5)
