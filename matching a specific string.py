""""
Link: https://www.hackerrank.com/challenges/matching-specific-string/problem?isFullScreen=true
"""

Regex_Pattern = r'[a-z]acker[a-z]ank'  # Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

