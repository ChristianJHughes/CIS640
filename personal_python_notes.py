w# A comment looks like this
""" A Multiline Comment
In Python looks like this.
"""

# Exponents 2^3
eight = 2 ** 3

# str() function converts non-strings into strings
StringVar = str(2)

# We can use the % opperator in the print function to substitute variables into string literals
var = "here"
var2 = "now"
print("come over %s %s" % (vkar, var2))

# Libraries are imported as so
from datetime import datetime
now = datetime.now()

# Get Text Input from the user
name = input("How's it Going?")
print(name)

# Check the contents of a string
str1 = "ABC"
print(str1.isalpha())
.lower() # Makes Lowercase
.upper() # Makes Uppercase

# Create functions using the def statement
def newFunc():
    print "example"

newFunc()

# Import math functions as follows
import math # This imports math. Thereafter you call functions as math.sqrt(), etc.
from math import sqrt # This imports a specific function or variable
from math import * # Universal import. Imports the entire library.


# Functions built in without imports
max(1,2,3) # Returns a the max of a list
min (1,2,3)
type("Cat") # Prints the type of the argument. In this case, it prints "String"

# Items can be added to a list with the .append() method.
newList = [1,2,3]
newList.append(4)
# Items can also be inserted into the list
newList.insert(1, 1.5)
# Search for the index of a particular item with the .index() method.
newList.index(1) #  1.5
# Sort a list
newList.sort()
# remove from a list (it searches for the item)
newList.remove(item)
# remove from a list (it removes the item at the given index)
newList.remove(index)

# Lists are passed to functions by reference -- any changes made in a function are done to the object.

# For-each loop
for item in listEx:
    print "cat" + item

# Delete itmes in a dictionary
del dict_name[key_name]

# The RANGE function creates a list of numbers in a fixed range. Often used in for loops.
# From Start UP TO BUT NOT INCLUDING stop
range(stop)
range(start,stop)
range(start,stop,step)
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

# While loop
loop_condition = True
while loop_condition:
    print "I am a loop"
    loop_condition = False

# While else loop
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

# The break statement will always exit a loop.
break

# For else loop. Else branch ONLY EXCECUTES if there is no break in the for loop (it exits normally)
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

# Example of a class in python.
# 'self' is the same as 'this' in many other languages.
class Fruit(object): # The parentheses is what class this class inherits from
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous): # Init is how you define a constructor
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False) # Creating a new instance of the object

lemon.description()
lemon.is_edible()
