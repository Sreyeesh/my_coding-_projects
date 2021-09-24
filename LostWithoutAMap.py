"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

"""

list_of_numbers = [1,2,3]

def maps(a):
    new_list_of_numbers =  []

    for i in range(len(a)):
        a[i] *= 2
        new_list_of_numbers += [a[i]]

    return new_list_of_numbers
    
print(maps(list_of_numbers))    


