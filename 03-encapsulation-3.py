#!/usr/bin/env python

# 03-encapsulation-3.py

# Here we look at another example, where we have three methods
# set_val(), get_val(), and increment_val().

# set_val() helps to set a value, get_val() prints the value,
# and increament_val() increments the set value by 1.

# We can still break encapsulation here by calling 'self.value'
# directly in an instance, which is **BAD**.

# set_val() forces us to input an integer. Even if we break encapsulation
# we're forced to call 'increment_val()` only if we have broken the
# encapsulation by passing an integer. ie.. `increment_val() will
# only work if we pass an int, be it by obeying encapsulation or
# breaking it.

class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val


    def get_val(self):
        print(self.val)

    def increment_val(self):
        self.val = self.val + 1
        print(self.val)

a = MyInteger()
a.set_val(10)
a.get_val()
a.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with an int
c = MyInteger()
c.val = 15
c.get_val()
c.increment_val()
print("\n")

# Trying to break encapsulation in a new instance with a str
b = MyInteger()
b.val = "MyString" # <== Breaking encapsulation, works fine
b.get_val()        # <== Prints the val set by breaking encap
b.increment_val()  # This will fail, since str + int wont work
print("\n")



