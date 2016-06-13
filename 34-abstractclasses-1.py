#!/usr/bin/env python

# 34-abstractclasses-1.py

# This code snippet talks about Abstract Base Classes (abc)

import abc

# Abstact Base Class defined below

class GetterSetter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, val):
        """Set a value in the instance"""
        return

    @abc.abstractmethod
    def get_val(self):
        """Get a return value from the instance"""
        return

# Abstract Base Class defined above ^^^

# Custom class inheriting from the above Abstract Base Class

class MyClass(GetterSetter):

    def get_val(self, input):
        self.val = input

    def get_val(self):
        return self.val


my_class = MyClass()
print(my_class)
