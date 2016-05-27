#!/usr/bin/env python

# 19-decorators-1.py

# In certain cases, an instance is necessarily not needed for a method in
# a class to be called. In such cases, we need not use it as a Bound method
# or in other words, Instance method.

# This is where Class methods come in. Class methods are used to access
# methods defined in a class without it being bound to the instance.

# In this example, we have two classes, class `A` and class `B`. 
# Each class has a method named 'method'.

# Class `A` is setting the method as a `staticmethod`, while class `B`
# leaves it as it is.


class A(object):
    @staticmethod
    def my_method(*argv):
        return argv


class B(object):
    def my_method(*argv):
        return argv

a = A()
print(a.my_method)

b = B()
print(b.my_method)

# More examples and use-cases will follow
