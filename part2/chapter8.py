# CHAPTER 8: LISTS AND DICTRIONARIES

# LISTS

# Python Lists have the main properties:
# 1) Ordered collections of arbitrary object ---> maintain left to right positional ordering
# 2) Accessed by offset ---> Possible since it is ordered consistently
# 3) Variable-Length, heterogeneous, and arbitrarily nestable ---> can change in size, have diff objects, can have lists
#   ## inside of lists
# 4) They are mutable ----> We can modify them in place
# 5) Arrays of object references ---> we hold pointers, not actual objects

# List Basics:
# Concatenating lists only work if its the same type of 'sequence object', i.e cant concatenate a list and a string
#   ## Otherwise an error occures where the list is turn into a string and then concatenated

# Changing Lists in Place:
# We can use slice assignemtnts and indexing to change a set of indicies in a list: L[0:2] = ['eat, 'more'] changes
#   ## L[0] and L[1], i.e it deletes the slice then inserts the new iterable object where the slice was before
# EX: L = [1,2,3], L[1:2] = [4,5] ---> L = [1,4,5,3] (it doesn't ovewrite the range above if its too much
# There can be methods that better suit this though (like insert, pop, remove)

# We can also delete elements using the 'del' keyword, i.e del L[0]
# BEWARE of methods that don't return lists, I'll have to get used to function signatures in python

# DICTIONARIES

# Properties of Python Dictionaries:
# 1) Accessed by Key, not Position - dicts are not reliably ordered, the associateon is used by keys
# 2) Unordered Collections of arbitrary objects - unordered, but can hold anything
# 3) Of the category mutable mapping - cant use sequence methods
# 4) Tableds of object references - Essentially a table of keys that correlate to a value (like a hash table)

# in lets you see if a key is in a dictionary, i.e 'key' in 'dictionaryName'
# We can modify dictionaries in place, adding/overwriting keys by assignment, and deleting key,value pairs with del
# Some key methods include values,keys, items(the key,value pairs), .get('keyName') to guarantee a value regardless of
# ##key existence, returns 'None' if a default is not specificed.
# A key can be any immutable object (we can't use a list reference)

# Here are a couple of ways to avoid missing-key errors:
# 1) Check if key exists via if check
# 2) Do a try catch
# 3) Do a .get with a default return value

# There are four ways to create dictionaries:
# 1) Literal Expression ---> {'name': 'bob'}
# 2) Assign Dynamically ----> D = {}, then D[key] = value
# 3) Constrcutor -----> D = dict(age= 40, name = 'sfsf) (keys need to be strings)
# 4) Initialize with list of key/value tuples ---> D = dict([('name, 'bob')])
# 5) Initialize a set of keys with default values ---> D = dict.fromKeys([1,2,3], 0)
# ### Can also use this with zip(keys, values), i.e dict(zip(keys, values))

# Dictionary Comprehensions
# D = {k: v for (k,v) in zip(['a'], [1])} ---> create a k: v entry for each (k,v) tupple that results from the zip
# D = {x: x** 2 for x in [1,2,3,4]}, D = { c.lower(){ c + '!' for c in ['spam']}
# We can have expressions to compute both keys and values in our comprehensions

# Dictonary Views
# dict fuctions keys, items, values return view objects instead of lists
# The key difference is that views are 'iterables' which generate values one at a time, retain original order of dict
#   #components, reflect future changes to the dectionary (it's linked almost), and have set operations
# vies use less memory by not being a list, but cannot use sort,indexing, and don't display the same
# The keys view is set like, the values  are not, while the items view is if the pairs are unique/hashable (i.e only
# # immutable objects)
# THINGS TO LOOK UP LATER:
# 1) List Methods
# 2) Dict Methods
# 3) Comprehensions as a whole, for lists/dicts/sets
# 4) Dict sorting and magnitude checks
