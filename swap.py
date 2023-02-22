#!/usr/bin/python3


def take_string(string):

    def recurse(string):
        if string == '':
            return ''

        output = recurse(string[2:])
        elements = list(string[0:2]) #take the first two elements of the string

        elements[0], elements[1] = elements[1], elements[0] #swap them

        string = ''.join(elements) + output #recreate the string
         
        return string

    result = recurse(string)

    return result

print(take_string('abcdefgh'))

