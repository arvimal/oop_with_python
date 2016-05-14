#!/usr/bin/env python3

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newvalue):
        set.val = newvalue

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count

# Instances

one = InstanceCounter(10)
two = InstanceCounter(20)
three = InstanceCounter(30)

for i in (one, two, three):
    print("Name of instance    : %s" % i)
    print("Value of object     : %s" % i.val)
    print("Number of instance  : %s\n" % i.get_count())

print("We can directly call a class method as 'Class.classmethod'")
print(InstanceCounter.get_count())