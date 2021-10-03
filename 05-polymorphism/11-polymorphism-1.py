#!/usr/bin/env python

# 11-polymorphism-1.py

# Polymorphism means having the same interface/attributes in different
# classes.

# Polymorphism is the characteristic of being able to assign
# a different meaning or usage in different contexts.
# A not-so-clear/clean example is, different classes can have
# the same function name.

# Here, the class Dog and Cat has the same method named 'show_affection'
# Even if they are same, both does different actions in the instance.
#
# Since the order of the lookup is
# 'instance' -> 'class' -> 'parent class', even if the
# 'class' and 'parent class' has functions with the same name,
# the instance will only pick up the first hit,
# ie.. from the 'class' and won't go to the parent class.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{0} eats {1}".format(self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("{0} goes after the {1}!".format(self.name, thing))

    def show_affection(self):
        print("{0} wags tail".format(self.name))


class Cat(Animal):
    def swatstring(self):
        print("{0} shreds more string".format(self.name))

    def show_affection(self):
        print("{0} purrs".format(self.name))


for a in (Dog("Rover"), Cat("Fluffy"), Cat("Lucky"), Dog("Scout")):
    a.show_affection()
