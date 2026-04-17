#!/usr/bin/env python

# encapsulation-1.py

# Encapsulation means to preserve data in classes using methods
# Here, we're setting the 'val' attribute through 'set_val()'.
# See the next example, `encapsulation-2.py` for more info

# In this example, we have two methods, `set_val` and `get_val`.
# The first one sets the `val` value while the second one
# prints/returns the value.


class MyClass(object):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        # print(self.value)
        return self.value


a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

a.get_val()
b.get_val()

# NOTE: If you run this code, it won't print anything to the screen.
# This is because, even if we're calling `a.get_val()` and `b.get_val()`,
# the `get_val()` function doesn't contain a `print()` function.
# If we want to get the output printed to screen, we should do any of
# the following:

# a) Either replace `return self.value` with `print(self.value)`
# or add a print statement **above** `return` as `print(self.value)`.

# b) Remove `return(self.value)` and replace it with `print(self.value)`
