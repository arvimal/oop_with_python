#!/usr/bin/env python

# 31-magicmethods-2.py

# In the backend, python is mostly objects and method
# calls on objects.

# To read more on magic methods, refer :
# http://www.rafekettler.com/magicmethods.html

my_list_1 = ["a", "b", "c"]

my_list_2 = ["d", "e", "f"]

print("\nCalling the `+` builtin with both lists")
print(my_list_1 + my_list_2)

print("\nCalling `__add__()` with both lists")
print(my_list_1.__add__(my_list_2))
