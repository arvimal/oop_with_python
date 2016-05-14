#!/usr/bin/env python


class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

    def test(self):
    	pass

