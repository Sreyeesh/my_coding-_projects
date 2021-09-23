"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
test
XO("zzoo") => false

"""


# Check to  see if a string has same amount 'x' and 'o'
# you can use count to count strings

s ='xo'

def xo(s):
    letters = s
    x_count = 0 
    o_count = 0 

    for i in letters:
        if i.lower() == 'x':
             x_count += 1
        elif i.lower() == 'o':
            o_count += 1

    return x_count == o_count 


print(xo(s))
  