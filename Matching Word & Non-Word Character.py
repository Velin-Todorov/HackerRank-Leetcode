"""
Link: https://www.hackerrank.com/challenges/matching-word-non-word/problem?isFullScreen=true
"""

Regex_Pattern = r"\w{3}\W\w{1,}\W\w{3}"	 # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())