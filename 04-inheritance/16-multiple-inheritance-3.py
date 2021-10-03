#!/usr/bin/env python

# 16-multiple-inheritance-3.py

# Python supports multiple inheritance
# and uses a depth-first order when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# Example for "Diamond Shape" inheritance
# Lookup can get complicated when multiple classes inherit
# from multiple parent classes.

# In order to avoid ambiguity while doing a lookup for a method
# in various classes, from Python 2.3, the MRO lookup order has an
# additional feature.

# It still does a depth-first lookup, but if the occurrence of a class
# happens multiple times in the MRO path, it removes the initial occurrence
# and keeps the latter.

# In the example below, class `D` inherits from `B` and `C`.
# And both `B` and `C` inherits from `A`.
# Both `A` and `C` has the method `dothis()`.

# We instantiate `D` and requests the 'dothis()' method.
# By default, the lookup should go D -> B -> A -> C -> A.
# But from Python 2.3, in order to reduce the lookup time,
# the MRO skips the classes which occur multiple times in the path.

# Hence the lookup will be D -> B -> C -> A.


class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(A):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()

print("\nPrint the Method Resolution Order")
print(D.mro())
