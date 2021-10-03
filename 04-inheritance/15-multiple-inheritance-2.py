#!/usr/bin/env python

# 15-multiple-inheritance-2.py

# Python supports multiple inheritance

# It uses a depth-first order when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# This is a second example, which shows the lookup of 'dothis()'.
# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

# As per the MRO output using depth-first search,
# it starts in class D, then B, A, and lastly C.

# Here we're looking for 'dothis()' which is defined in class `C`.
# The lookup goes from D -> B -> A -> C.

# Since class `A` doesn't have `dothis()`, the lookup goes back to class `C`
# and finds it there.


class A(object):
    def dothat(self):
        print("Doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("\nDoing this in C")


class D(B, C):
    """Multiple Inheritance,
    D inheriting from both B and C"""

    pass


d_instance = D()

d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())
