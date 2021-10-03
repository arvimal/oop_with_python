#!/usr/bin/env python

# 30-magicmethods-1.py

# In the backend, python is mostly objects and method
# calls on objects.

# Here we see an example, where the `print()` function
# is just a call to the magic method `__repr__()`.


class PrintList(object):
    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())
