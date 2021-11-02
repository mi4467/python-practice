# CHAPTER 9: TUPLES, FILES, AND EVERYTHING ELSE

# TUPLES

# Tuples have the following properties
# 1) Ordered collection of arbitrary objects
# 2) Accessed by offset
# 3) Immutable sequence
# 4) Fixed length, heterogeneous, arbitrarily nestable
# 5) Array of object references

# A tuple with a single element needs a comma, otherwise its expressed as a literal
# Slicing/sorting/etc returns new tuples

# OBJECT FLEXIBILITY

# Lists, dictionaries, and tuples can hold any kind of object
# Sets can only hold immutable objects
# Lists, dictionaries and sets are mutable
# Strings and tuples are immutable
# Lists, dictionaries, and tuples can be arbitrarily nested
# Lists, dictionaries, and sets can have dynamic sizing

# COMPARISIONS, EQUALITY, AND TRUTH

# Python equality relative magnitude, works by inspecting all parts of the compound objects untill a result is found
# ## BASICALLY ITS NOT BY REFERENCE, THE REFERENCE CHECK IS REPLACES BY 'IS'
# 'name' is 'name' is true since python caches the string in memory and makes them in the same memory location

# Python compares the following types by:
# 1) Numbers - Compareds by relative magnitude after conversions
# 2) String - Compared lexographically, smaller words win
# 3) Lists/Tuples - Compared by each value, smaller sequence wins
# 4) Sets - Equal if both sets contain the same elements
# 5) Dictionaries - Equal if sorted key value pairs are equal
# 6) NonNumeric Mixed Types - Throws errors (i.e 1 and 'spam')

# THE MEANING OF TRUE AND FALSE IN PYTHON

# Numbers are false if zero, true otherwise
# Other objects are false if empty, true otherwise

# The 'None' object is also considered to be false

# COMMON MISTAKES PEOPLE MAKE
# 1) Assignments create references not copies
# 2) Repitition adds one level deep
# 3) Cyclic data structures - If an object holds a reference to itself (python will print [...])
# 4) Immutable types cannot be changed in place


# THINGS TO LOOK UP LATER
# 1) Tuple methods
# 2) Named tuple
# 3) Look up Files stuff later
# 4) How to make copies of specific objects (take note which ones make top level copies, and which ones do nested copies)
# 5) Pythons Type Hiearchies chart