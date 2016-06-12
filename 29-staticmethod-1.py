#!/usr/bin/env python3


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