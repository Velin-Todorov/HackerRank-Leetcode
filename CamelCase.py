"""
Link to task:
https://www.hackerrank.com/challenges/camelcase/problem?isFullScreen=true

"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    number_of_words = 1
    capital_words = [x for x in s if x.isupper()]

    number_of_words += len(capital_words)
    return number_of_words


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
