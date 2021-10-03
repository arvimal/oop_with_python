#!/usr/bin/env python

# 14-multiple-inheritance-1.py

# Python supports multiple inheritance and uses a depth-first order
# when searching for methods.
# This search pattern is call MRO (Method Resolution Order)

# This is the first example, which shows the lookup of a common
# function named 'dothis()', which we'll continue in other examples.

# As per the MRO output, it starts in class D, then B, A, and lastly C.

# Both A and C contains 'dothis()'. Let's trace how the lookup happens.

# As per the MRO output, it starts in class D, then B, A, and lastly C.

# class `A` defines 'dothis()' and the search ends there. It doesn't go to C.

# The MRO will show the full resolution path even if the full path is
# not traversed.

# The method lookup flow in this case is : D -> B -> A -> C


class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


d_instance = D()
d_instance.dothis()  # <== This should print from class A.

print("\nPrint the Method Resolution Order")
print(D.mro())
