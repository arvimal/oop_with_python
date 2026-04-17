#!/usr/bin/env python

# 37-method-overloading-1.py

# Reference: O'Reilly Learning Path:
# http://shop.oreilly.com/product/0636920040057.do
# Chapter 24 : Method Overloading - Extending and Providing

# This code is an example on how we can extend a method inherited by
# a child class from the Parent class.

# 1) We have defined `MyClass()` as an abstract class,
# and it has three methods, my_set_val(), my_get_val(), and print_doc().
# 2) MyChildClass() inherits from MyClass()
# 3) MyChildClass() extends the parent's my_set_val() method
# by it's own my_set_val() method. It checks for the input,
# checks if it's an integer, and then calls the my_set_val()
# method in the parent.

# 4) The print_doc() method in the Parent is an abstract method
# and hence should be implemented in the child class MyChildClass()


import abc


class MyClass(object):

    __metaclass__ = abc.ABCMeta

    def my_set_val(self, value):
        self.value = value

    def my_get_val(self):
        return self.value

    @abc.abstractmethod
    def print_doc(self):
        return


class MyChildClass(MyClass):
    def my_set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(MyChildClass, self).my_set_val(self)

    def print_doc(self):
        print("Documentation for MyChild Class")


my_instance = MyChildClass()
my_instance.my_set_val(100)
print(my_instance.my_get_val())
print(my_instance.print_doc())
