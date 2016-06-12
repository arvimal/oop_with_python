#!/usr/bin/env python3

# 29-staticmethod-1.py

# Refer
# https://arvimal.wordpress.com/2016/06/12/instance-class-static-methods-object-oriented-programming/

# Static methods are functions/methods which doesn’t need a binding to a class or an instance.
# Static methods, as well as Class methods, don’t require an instance to be called.
# Static methods doesn’t need  self or cls as the first argument since it’s not bound to an instance or class.
# Static methods are normal functions, but within a class.
# Static methods are defined with the keyword @staticmethod above the function/method.
# Static methods are usually used to work on Class Attributes.


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            print("Entered value is not an INT, value set to 0")
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

print(a.val)
print(b.val)
print(c.val)
print(a.filterint(100))
