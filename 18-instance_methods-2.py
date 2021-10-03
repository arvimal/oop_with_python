#!/usr/bin/env python3

# 18-instance_methods.py

# Instance methods are the normal way of accessing methods, seen in all
# classes till now. ie.. by instantiating instances from a class, and
# access the methods within the class. The usage of `self` is very
# important in instance methods due to `self` being a hook/handle to the
# instance itself, or the instance itself.

# We look into a previous example, once more, to understand `Instance methods`.

# We have an __init__() constructor, and three methods within the
# `InstanceCounter` class.

# Three instances a, b, and c are created from the class `InstanceCounter`.

# Since the methods defined in the class are accessed through the
# instances 'a', 'b', and 'c', these methods are called 'Instance
# methods'.

# Since the instance is bound to the methods defined in the class by the
# keyword `self`, we also call `Instance methods` as 'Bound methods'.

# In the code below, the instance is `obj` (the iterator) and we access
# each method as `obj.set_val()`, `obj.get_val()`, and `obj.get_count`.


class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count


a = InstanceCounter(5)
b = InstanceCounter(10)
c = InstanceCounter(15)

for obj in (a, b, c):
    print("Value of object: %s" % (obj.get_val))
    print("Count : %s " % (obj.get_count))
