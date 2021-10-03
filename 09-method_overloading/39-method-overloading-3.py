#!/usr/bin/env python

# 39-method-overloading-3.py

# We've seen that inherited methods can be overloaded.
# This is possible using in-built functions as well.

# Let's see how we can overload methods from the `list` module.


class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError
        if index > 0:
            index -= 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError
        if index > 0:
            index -= 1
        list.__setitem__(self, index, value)


x = MyList(["a", "b", "c"])
print(x)
print("-" * 10)

x.append("d")
print(x)
print("-" * 10)

x.__setitem__(4, "e")
print(x)
print("-" * 10)

print(x[1])
print(x.__getitem__(1))
print("-" * 10)

print(x[4])
print(x.__getitem__(4))
