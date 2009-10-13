#!/usr/bin/env python
# pound sign is a comment

# booleans
False
True

# other objects

None

# assert
assert(True) #raises exception if False
assert(False or True)
# some objects are "falsy"
assert(not [])
assert(not "")
assert(not 0)
assert(not {})


# exceptions
try:
    assert(False and True) # scope is designated by : and 4 spaces
except:
    pass # pass helps us exit scope despite the above rules


# variables
x = 10
y = 5


# operations
assert(x - y == 5)
assert(x + y == 15)
assert(x * y == 50)
assert(x / y == 2)
assert(x ** y == 100000)

# Strings

s = "abcdefg"

## object methods
assert(s.islower())
assert(not s.upper().islower())

dir(s) # returns a list of all methods

s2 = "a,b,c,d,e,f,g"
assert(s2.split(",") == ["a", "b", "c", "d", "e", "f", "g"])


# Dictionaries / Hashes / Assosciative arrays
d = {"key": "value"}

assert(d["key"] == "value")
assert(d.keys() == ["key"])
assert(d.values() == ["value"])

d["key"] = "new_value"
assert(d["key"] == "new_value")

d["new_key"] = 10

assert(d["new_key"] == 10)


# Lists
l = [1, 2, 3, 4, 5]
l2 = range(1,6)
assert(l == l2)

## list itteration ##
for i in l:
    assert(i)


## list comprehension ##
### creates a new list from an old list ###
l3 = [i for i in l]
assert(l3 == l)

l4 = [i*10 for i in l]
assert(l4 == [10,20,30,40,50])

l5 = [i for i in l if i > 3] # filter entries greater than 3
assert(l5 == [4,5])


# functions
def my_function(x):
    """
    You can put any string after a function definition. This will be used to
    create help documentation for the function.
    """
    return x * x

assert(my_function(10) == 100)

## keword arguements ##

def my_other_function(x = 10, y = 5):
    return x * y    

assert(my_other_function() == 50)
assert(my_other_function(x=2) == 10)
assert(my_other_function(y=4) == 40)
assert(my_other_function(x=2, y=4) == 8)


# classes

class ParentClass(object):
    pass

class MyClass(ParentClass):
    """
    Just like doc strings on functions
    """

    def __init__(self, x):
        """
        The same applies to methods
        """
        self.my_value = x

    def my_method(self, y):
        return self.my_value * y

    def my_other_method(self):
        return self.my_method(6)

m = MyClass(10)
assert(m.my_value == 10)
assert(m.my_method(5) == 50)
assert(m.my_other_method() == 60)


# python packages and the standard library
# standard library documentation http://docs.python.org/library/

import re # regex support
import datetime # date and time support
import random # random value support
import os # os functions support
from os import path # only include the modules you want (and path support)
import hashlib # hash support (hmac, sha1, md5)
import subprocess # call out to new processes support
import email # email support
import json # email support

# use pip / easy install to get new packages not in standard library

# execute the following commands to get the python package manager installed
#   > wget http://pypi.python.org/packages/source/p/pip/pip-0.5.1.tar.gz#md5=d4bdaa5f5f5bf8c6263ace75a0882232
#   > tar -xzvpf pip-0.5.1.tar.gz
#   > sudo python setup.py install
#   > sudo pip install ipython

#subprocess.call(["wget", "http://pypi.python.org/packages/source/p/pip/pip-0.5.1.tar.gz#md5=d4bdaa5f5f5bf8c6263ace75a0882232"])
#subprocess.call(["tar", "-xzvpf", "pip-0.5.1.tar.gz"])
#subprocess.call(["python", "setup.py", "install"])
