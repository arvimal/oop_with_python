#!/usr/bin/env python

# 42-super-3.py

# super() and __init__()

# Refer
# https://arvimal.wordpress.com/2016/07/01/inheritance-and-super-object-oriented-programming/

# http://www.blog.pythonlibrary.org/2014/01/21/python-201-what-is-super/


class A(object):
    def foo(self):
        print("A")


class B(A):
    def foo(self):
        print("B")


class C(A):
    def foo(self):
        print("C")
        super(C, self).foo()


class D(B, C):
    def foo(self):
        print("D")
        super(D, self).foo()


d = D()
d.foo()
