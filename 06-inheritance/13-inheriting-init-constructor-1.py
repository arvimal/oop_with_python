#!/usr/bin/env python

# 13-inheriting-init-constructor-1.py

# This is a normal inheritance example from which we build
# the next example. Make sure to read and understand the
# next example '14-inheriting-init-constructor-2.py'.


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


d = Dog("Roger")
print("The dog's name is", d.name)
d.fetch("frizbee")
