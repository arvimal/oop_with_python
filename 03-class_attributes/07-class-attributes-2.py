#!/usr/bin/env python

# 07-class-attributes-2.py

# The code below shows two important points:

# a) A class attribute can be overridden in an instance, even
# though it is bad due to breaking Encapsulation.

# b) There is a lookup path for attributes in Python. The first being
# the method defined within the class, and then the class above it.

# We are overriding the 'classy' class attribute in the instance 'dd'.
# When it's overridden, the python interpreter reads the overridden value.
# But once the new value is deleted with 'del', the overridden value is no longer
# present in the instance, and hence the lookup goes a level above and gets it from
# the class.


class YourClass(object):
    classy = "class value"


dd = YourClass()
print(dd.classy)  # < This should return the string "class value"

dd.classy = "Instance value"
print(dd.classy)  # This should return the string "Instance value"

# This will delete the value set for 'dd.classy' in the instance.
del dd.classy
# Since the overriding attribute was deleted, this will print 'class value'.
print(dd.classy)
