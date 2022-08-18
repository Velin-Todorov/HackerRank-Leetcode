"""Link to task: https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=false"""
import re

regex = r'^[+-.]?\d*\.{1}\d+'

for _ in range(int(input())):
    string = input()

    result = re.fullmatch(regex, string)

    if result:
        print(True)
    else:
        print(False)