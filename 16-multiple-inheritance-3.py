#!/usr/bin/env python

# multiple-inheritance-3.py

# Python supports multiple inheritance
# and uses a depth-first order when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# Example for "Diamond Shape" inheritance
# Lookup can get complicated when multiple classes inherit
# from multiple parent classes.

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