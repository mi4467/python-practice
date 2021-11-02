# CHAPTER 5: Numeric Types

# NUMBER NOTES
# 1) Integers/Floating point literals:
#   ## Integers are written as strings of decimal digits, floating points have a decimal and/or exponent
#   ## If a number is written with a decimal/floating point, python makes it floating point object
#   ## From python #, integers are a single type and no longer need L/l to signify more its

# NUMERIC TOOLS
# 1) Operators -> +,-,*,/,>>,**,&, etc
# 2) Mathmatical functions -> pow, abs, round, int, hex, bin, etc
# 3) Utility Modules -> random, math, etc

# There is an order of precedency, pretty similar to that of java

# Mixed types are converted up, i.e integer + float returns a float, with the integer turning int o a float
#   ## It converts up the operands, then computes

# VARIABLES AND BASIC EXPRESSIONS
# 1) Variables are created when they are first assigned values
# 2) Variables are replaced with their values when used in expressions
# 3) Variables must be assigned before they can be used in expressions
# 4) Variables refer to objects and are never declared ahead of time

# Variables need to be initialized before we can operate on them

# COMPARISONS

# Python lets you chain comparisons together, say X = 2, Y = 4, Z = 6, then we can do
# 1) X < Y < Z --> true
# 2) X < Y and Y > Z ---> false (we use and not &&)
# Note: Precision can mess things up

# DIVISION: CLASSIC, FLOOR, and TRUE
# 1) X/Y --> normal division, doesnt remove floating points
# 2) X // y ---> floor division, removes floating point (but can still be a floating point type),
# ## it rounds to the closes whole number below the result

# BITWISE OPERATIONS
# # <<, |, & operators

# SETS

# set([list]) or {value, value2, ....valueN}
# {} is still a legal set

# We cannot put mutable objects in a set, i.e we can not have a list or a dict in a set., tuples are fine
# We can use set comprehensions, they wrok the same like list comprehensions, just have {} around instead of []

# BOOLEANS

# True and False behave exactly like 1 and 0, except the print logix is different\
#  # can be used directly in a whjile loop or a comparison

# Names have no types, objects have type designator and reference counter, used for type check and garbage collection
# A Name is assigned a reference to the object, not the object itself

# EQUALITY CHECKS
# # L == M checks to see if same values, L is M checks to see if same objects

# THINGS TO LOOK UP LATER
# 1) Hexasecimal/octal/binary/complex literals
# 2) Math library/ Random library
# 3) Copy module for object copying
