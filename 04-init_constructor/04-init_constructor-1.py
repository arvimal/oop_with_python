#!/usr/bin/env python

# 04-init_constructor.py

# __init__() is a constructor method which helps to
# set initial values while instatiating a class.

# __init__() will get called with the attributes set in __init__(),
# when a class is instantiated.

# The '__' before and after the method name denotes that
# the method is private. It's called private or magic methods
# since it's called internally and automatically.


class MyNum(object):
    def __init__(self):
        print("Calling the __init__() constructor!\n")
        self.val = 0

    def increment(self):
        self.val = self.val + 1
        print(self.val)


dd = MyNum()
dd.increment()  # will print 1
dd.increment()  # will print 2
