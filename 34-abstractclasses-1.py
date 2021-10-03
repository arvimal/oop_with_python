#!/usr/bin/env python

# 34-abstractclasses-1.py

# This code snippet talks about Abstract Base Classes (abc).

# The `abc` module provides features to create
# Abstract Base Classes.

# To create an Abstract Base Class, set the `__metaclass__` magic method
# to `abc.ABCMeta`. This will mark the respective class as an Abstract
# Base Class.

# Now, in order to specify the methods which are to be enforced on the
# child classes, ie.. to create Abstract Methods, we use the decorator
# @abc.abstractmethod on the methods we need.

# The child class which inherits from an Abstract Base Class can implement
# methods of their own, but *should always* implement the methods defined in
# the parent ABC Class.

import abc


class My_ABC_Class(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        return

    @abc.abstractmethod
    def get_val(self):
        return


# Abstract Base Class defined above ^^^

# Custom class inheriting from the above Abstract Base Class, below


class MyClass(My_ABC_Class):
    def set_val(self, input):
        self.val = input

    def get_val(self):
        print("\nCalling the get_val() method")
        print("I'm part of the Abstract Methods defined in My_ABC_Class()")
        return self.val

    def hello(self):
        print("\nCalling the hello() method")
        print("I'm *not* part of the Abstract Methods defined in My_ABC_Class()")


my_class = MyClass()

my_class.set_val(10)
print(my_class.get_val())
my_class.hello()
