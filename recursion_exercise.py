#!/usr/bin/python3
"""
1. What are we going to make smaller?
2. What are the variables that go into our function?
3. What are we modifying the body of a function?

"""

def take_string(string):
    
    count = 0

    def recurse(string):
        nonlocal count
        if string == '':
            return count

        char = string[0]
        string = string.replace(char, '', 1)
        count += 1

        return recurse(string)

    result = recurse(string)
    return result

take_input = input('Please enter a string to compute: ')
print(f'The len of your string is {take_string(take_input)}')
 

