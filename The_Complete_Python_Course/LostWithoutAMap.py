"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

"""

"""
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]

"""

list_of_numbers = [1,2,3]

def maps(a):
    new_list_of_numbers =  []

    for i in range(len(a)):
        # print('this is a number ',i)
        a[i] *= 2
        # print('numbers',a[i])
        new_list_of_numbers += [a[i]]
        # print('more numbers',new_list_of_numbers)

    return new_list_of_numbers
    
print(maps(list_of_numbers))  
