#!/usr/bin/env python

# 37-method-overloading-1.py

# Reference: O'Reilly Learning Path:
# http://shop.oreilly.com/product/0636920040057.do
# Chapter 24 : Method Overloading - Extending and Providing

# This code is an example on how we can extend a method
# defined in a Parent class, in the Child class.

# 1) We have defined `GetSetParent()` as an abstract class,
# and it has three methods, set_val(), get_val(), and showdoc().
# 2) GetSetInt() inherits from GetSetParent() 
# 3) GetSetInt() extends the parent's set_val() method
# by it's own set_val() method. It checks for the input,
# checks if it's an integer, and then calls the set_val()
# method in the parent.

# 4) The showdoc() method in the Parent is an abstract method
# and hence should be implemented in the child class GetSetInt()


import abc


class GetSetParent(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return


class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(self)

    def showdoc(self):
        print("GetSetInt object {0}), only accepts integer values".format(
            id(self)))


