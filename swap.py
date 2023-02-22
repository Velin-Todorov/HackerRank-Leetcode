#!/usr/bin/python3


def take_string(string):
    
    idx = 0

    def recurse(string):
        nonlocal idx

        if idx + 1 == len(string):
            return string
        
        str_lst = [string]

        str_list[idx], str_list[idx + 1] =  str_list[idx + 1], str_list[idx]

        string = ''.join(str_list)

        return recurse(string)

    result = recurse(string)

    return result

print(take_string('abcdefgh'))

