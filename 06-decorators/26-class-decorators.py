#!/usr/bin/env python

# 26-class-decorators.py

# Reference : https://www.youtube.com/watch?v=Slf1b3yUocc
# Talk by Mike Burns

# Till the previous examples, we saw function decorators.
# But decorators can be applied to Classes as well.
# This example deals with class decorators.

# NOTE: If you are creating a decorator for a class, you'll it
# to return a Class.

# NOTE: Similarly, if you are creating a decorator for a function,
# you'll need it to return a function.


def honirific(cls):
    class HonirificCls(cls):
        def full_name(self):
            return "Dr. " + super(HonirificCls, self).full_name()

    return HonirificCls


@honirific
class Name(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return " ".join([self.first_name, self.last_name])


result = Name("Vimal", "A.R").full_name()
print("Full name: {0}".format(result))


# This needs further check. Erroring out.
