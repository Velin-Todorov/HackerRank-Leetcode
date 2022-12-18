import re

n = int(input())

for i in range(n):
    line = input()
    result_v4 = re.fullmatch('(?:[\d, \.]+)', line)
    result_v6 = re.fullmatch('(?:[a-z0-9:]+:+)+[a-z0-9]+', line)

    if result_v4:
        print('IPv4')
    elif result_v6:
        print('IPv6')
    else:
        print('Neither')

