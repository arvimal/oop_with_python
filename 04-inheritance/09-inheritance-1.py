#!/usr/bin/env python

# 09-inheritance-1.py

# The code below shows how a class can inherit from another class.
# We have two classes, `Date` and `Time`. Here `Time` inherits from
# `Date`.

# Any class inheriting from another class (also called a Parent class)
# inherits the methods and attributes from the Parent class.

# Hence, any instances created from the class `Time` can access
# the methods defined in the parent class `Date`.


class Date(object):
    def get_date(self):
        print("2016-05-14")


class Time(Date):
    def get_time(self):
        print("07:00:00")


# Creating an instance from `Date`
dt = Date()
dt.get_date()  # Accesing the `get_date()` method of `Date`
print("--------")

# Creating an instance from `Time`.
tm = Time()
tm.get_time()  # Accessing the `get_time()` method from `Time`.
# Accessing the `get_date() which is defined in the parent class `Date`.
tm.get_date()
