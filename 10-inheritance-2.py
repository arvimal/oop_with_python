#!/usr/bin/env python

# 10-inheritance-2.py

# The code below shows another example of inheritance
# Dog and Cat are two classes which inherits from Animal.
# This an instance created from Dog or Cat can access the methods
# in the Animal class, ie.. eat().

# The instance of 'Dog' can access the methods of the Dog class
# and it's parent class 'Animal'.

# The instance of 'Cat' can access the methods of the Cat class
# and it's parent class 'Animal'.

# But the instance created from 'Cat' cannot access the attributes
# within the 'Dog' class, and vice versa.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("%s is eating %s" % (self.name, food))


class Dog(Animal):
    def fetch(self, thing):
        print("%s goes after the %s" % (self.name, thing))


class Cat(Animal):
    def swatstring(self):
        print("%s shred the string!" % self.name)


d = Dog("Roger")
c = Cat("Fluffy")

d.fetch("paper")
d.eat("dog food")
print("--------")
c.eat("cat food")
c.swatstring()

# The below methods would fail, since the instances doesn't have
# have access to the other class.

c.fetch("frizbee")
d.swatstring()
