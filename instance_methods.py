#!/usr/bin/env python3

class PrintName(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        """

        :rtype: basestring
        """
        print("Hello %s" % self.name)

printname = PrintName("Arthur")
printname.get_name()

for i in ["Vimal", "Vineeth", "Vyshakh"]:
    name = PrintName(i)
    name.get_name()