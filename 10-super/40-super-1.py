#!/usr/bin/env python

# 40-super-1.py

# This is an example on how super() works
# in Inheritance.

# For more step-by-step details, refer :
# https://arvimal.wordpress.com/2016/07/01/inheritance-and-super-object-oriented-programming/


class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But...")
        # Calling the `func()` method from the Parent class.
        super(ChildClass, self).func()


my_instance_2 = ChildClass()
my_instance_2.func()
