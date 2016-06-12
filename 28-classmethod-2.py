#!/usr/bin/env python

# 28-classmethod-2.py

# Classmethods are decorators which are inbuilt in Python.
# We decorate a function as a classemethod using the decorator
# @classmethod.

# Class methods are used for functions which need not be
# called via an instance. Certain use cases may be:

# a) Creating instances take resources, hence the methods/functions
# which need necessarily


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

a = InstanceCounter(10)
print("\nValue of object : %s" % a.get_val())
print(InstanceCounter.get_count())

b = InstanceCounter(20)
print("\nValue of object : %s" % b.get_val())
print(InstanceCounter.get_count())

c = InstanceCounter(40)
print("\nValue of object : %s" % c.get_val())
print(InstanceCounter.get_count())
