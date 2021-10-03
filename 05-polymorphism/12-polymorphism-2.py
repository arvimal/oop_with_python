#!/usr/bin/env python

# 12-polymorphism-2.py

# Another example for Polymorphism are the several inbuilt
# functions in Python. Take for example, the builtin function
# called 'len'.

# 'len' is available for almost all types, such as strings,
# ints, floats, dictionaries, lists, tuples etc..
# When len is called on a type, it actually calls the inbuilts
# private function 'len' on that type or __len__

# Every object type that supports 'len' will have a private
# 'len' function inbuilt.

# Hence, for example, a list type already has a 'len()'
# function inbuilt in the Python code, and when you run the
# len() function on the data type, it checks if the len
# private function is available for that type or not.
# If it is available, it runs that.

text = ["Hello", "Hola", "helo"]
print(len(text))

print(len("Hello"))
print(len({"a": 1, "b": 2, "c": 3}))
