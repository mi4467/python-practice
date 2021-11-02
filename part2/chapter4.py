# CHAPTER 4: INTRODUCING PYTHON OBJECT TYPES

# INTRODUCTION

# Python programs can be decomposed into the following:
# 1) Programs are made up of modules
# 2) Modules are made up of statements
# 3) Statements contain expressions
# 4) Expressions create and process objects

# Built in objects
# 1) Numbers - 1234, 3.1415, Decimal(), Fraction(), ob111 , i.e hella number types
# 2) Strings - 'bob', "biob's"
# 3) Lists - [1, [2, 'three'], 4.5], list(range(10))
# 4) Dictionaries - {'food' : 'spam'}, dict(hours=10)
# 5) Files - open('eggs.txt')
# 6) Sets - set('abc')
# 7) Other types like booleans, Types, none
# 8) Functions, Modules, Classes (i.e program unit types)

# Python is dynamically typed, once an object is created, the operations its born with is binded to it (i.e when the cod
# e is run not when it is compiled. Additionally python objects are strongly typed, it can only preform valid operations
# for the object

# NUMBERS

# Python includes the following types of numbers
# 1) Integers
# 2) Floating point
# 3) Complex Numbers (i.e imaginary parts)
# 4) Decimals (i.e fixed percision)
# 5) Rationsals (with numerator/denominator)...not sure what this is
# 6) Sets - what is this....

# Python has the following normal mathematical operations
# 1) + - Add
# 2) * - Multiply
# 3) ** - power
# 4) - - subtract
# 5) / - divide

# Objects in python have two representations:
# 1) str - A user friendly representation
# 2) repr - The as code representation

# Other interesting number modules are:
# Math (via import math)
# random (via import random)

# STRINGS

# Strings are known as a 'sequence', i.e n ordered sequence of one-character strings

# Strings are immutable, they cannot be changed once they arte defined

# We can use len('sen') to find the length of a string -- len is a built in function

# Python has neat indexing tricks:
# to access first element --> s[0]
# to access starting from last element use negatives --> s[-1] = last element
# We can also do len(element)-1 but its more faulty
# Slicing -> If we want a section of our element, here are some examples
#   ## S[1:3] means elements 1 and 2, but not 3 and after or 0, i.e inclusive of start but not the end
#   ## S[:5] means elements 0, 1, 2 , 3, 4, but not 5 and after
#   ## S[:] means copy the entire thing
#   ## S[:-1] means all the way except last character

# We can also concatenate strings directly, take S = 'Spam', we can
#   ## S + 'xt' = 'spamxt'
#   ## S*3 = 'SpamSpamSpam', i.e concatenate with itself 3 times

# IMMUTABILITY

# Immutable Types Include:
# 1) Numbers
# 2) Strings
# 3) Tuples

# Mutable Types Include:
# 1) List
# 2) Dictionaries
# 3) Sets
# 4) Objects born from classes we make

# TYPE SPECIFIC METHODS

# Python core types have their own type methods, for example a string has .find, .replace, etc

# There are also string formatting methods, just look up later to see whats our standards

# GETTING HELP

# To see the list of methods of an object call dir(S)
#   ##You might find functions with double underscores, they represent the implementation of the object and is avail
#   ##ble to support customization

# To see what a function does, do help(Object.functionName)

# LISTS

# Lists are a positionally ordered collection of arbitrarily typed objects
#   ## No fixed size and are mutable

# Sequence Operations are as follows, take L = [123, 'spam', 1.23]
# 1) len(L) = 3 ---> Gives the number of elements in the list
# 2) Normal Indexing stuff like we talked about earlier
# 3) L + [4] = [123, 'spam', 1.23, 4] (same reference) ---> concatenation of lists
# 4) L*2 = [123, 'spam', 1.23, 123, 'spam', 1.23] ---> just appending the list to itself

# Lists have their own built in methods, like sort, append, pop, push
# Python lists still give out of bounds errors

# Nesting
#   ##Python can have nested lists (i.e kinda like a multidemensional array), access by [row][col]

# COMPREHENSIONS

# List comprehensions are expressions derived from set notation

# Examples:
# 1) Grab a column in a matrix ---> col2 = [row[1] for row in M] (means for each row in M, grab row[1])
# 2) Perform an operation for each element we grab ---> col2 = [row[1] + 1 for row in M]
# 3) Filter out items ---> col2 = [row[1] for row in M if row[1] % 2 == 0]

# More complex examples:
# 1) diag = [M[i][i] for in in [0,1,2]] ---> collect the diagonal elements, in is a key word

# Comprehensions offer performance boosts, and can be used to make lists, sets, and dictionaries

# We can also use comprehensions to make generators (i.e an iterator almost), by wrapping a comprehension with parenthsis instead of brackets
#   ## G = (sum(row) for row in M) ---> next(G) gives the most recent unseen value

# Other Helpful Methods
# 1) list(operation) makes the return values into a list
# 2) map(function, values) returns the values (not in a list) for each value as function(value)

# DICTIONARIES

# Dictionaries are like maps in java, order is not reliable

# Dictionary syntax : D = {'food' : 'Spam', 'color': 'pink'} or dict(name='bob', age=40) (i.e a constructor)
# We can index a dictionary by keys like D['food']
# We can write/overwrite a dictionary by: D['keyName'] = value;
# Fetching a nonexistent key is a mistake, and will throw an error
#   ## we can use the in key word, i.e 'keyName' in dictName returns a boolean on if the key exists
#   ## aside from an if test we can also do.get('keyName', defaultValue), which returns default value if not found
# Keys are not sorted, but we might want to process them in some order, so we can:
#   ## grab keys in a list, sort, then iterate list(D.keys()).sort()
#   ## do for key in sorted(D), where sorted is a built in function that gives the keys

# ITERATION AND OPTIMIZATION

# An object is iterable if it is physically stored in a sequence or an object that generates values one at a time, i.e
# ## they support they respond to the 'iter' call and produce values in response to 'next' calls, and raise an exception
# ## once all values are exhausted

# TUPLES

# Tuples are lists that cannot be changed, i.e they are immutable
# Tuple syntax ---> T = (1,2,3,4), i.e use parenthesis instead of brackets
#   ## One item tuples require a comma, i.e (1,)
# We can index/concatenate like before, but they can produce new objects

# FILES

# File objects are Python code's main interface to eternal files.
# To create a file object, we use the 'open' method like so:
#   ## f = open('fileName.extension', 'accessMode') (very similar to java)
# We have functions like write, close, read, readline, etc

# SETS

# Unordered collections of unique and immutable objects
# Set Syntax ----> set('spam') or {'sf', 'sdgsg'} , basically sets are in brackets
# We can do set logic like & (intersection), | (union), - (removal), + (add)

# BOOLEANS

# Is either 'True' or 'False', 'None' is used as a placeholder


# THINGS I SKIPPED OVER SINCE IT WOULD BE OVERLOAD AND I CAN LOOK UP LATER
# 1) String Formatting
# 2) Unicode String
# 3) Pattern Matching
# 4) Binary Bytes Files
# 5) Unicode Text Files
# 6) Rationsal/Decimal/Faction nmmbers




