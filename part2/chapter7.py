# CHAPTER 7: STRING FUNDAMENTALS

# Strings are immutable
# Single quotes and double quotes are the same, single quotes are preferred
# Python implicitly concatenates strings that are not comma separated, if comma separated then its a tuple
# If python cannot recognize the next character on an escape sequence, it will just show a \
# If I want to use a raw string do r'stringliteral', which will turn off the escape mechanism
#   ## Limits to raw strings, a raw string cannot end in a odd number of backslashes(it needs to have a matching escape)
# Triple quotes is used for multiline blocks of text: """Hi. my anem."""
#   ## Useful for JSON/HTML literals, or error messages

# TYPES OF SLICING
# 1) Indexing S[i] fetcheses components at offsets
#   ## The first item is at offset 0
#   ## Negative Indexes mean to count backward from the end
#   ## s[0] gets the first item, s[-2] gets the second to last item
# 2) Slicing S[i:j]
#   ## Lower bound inclusive, upper bound exclusive
# 3) Extended Slicing S[i:j:k]
#   ## Accepts a step k (default is 1)
#   ## S[1:10:2] means starting at 1 grab every 2nd element up to but not including 10
#   ## S[::-1] basically reverses to elements in the list, S[5:1{-1] grabs elements in reverse
# NOTE: We can also use a slice object (start:end:stride(optional))

# TYPES SHARE OPERATION SETS BY CATEGORIES
# There are three major types and operation categories in python, each share their own generic implementation for
# ## common methods like adding/multiply/index/slicing/concatentation/etc
# 1) Numbers (Integers/floating ppoints/decimals/fractions, etc)
# 2) Sequences (Lists, tuples, strings)
# 3) Mappings (dictionaries)

# THINGS TO LOOK UP LATER
# 1) String Formatting
# 2) String methods (theres a table, but I can also foind the doc later)
# 3) String Conversion Tools