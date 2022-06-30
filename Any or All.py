n = int(input())
integers = [int(x) for x in input().split()]
result1 = True if all(x > 0 for x in integers) and any(x for x in integers if str(x) == str(x)[::-1]) else False

print(result1)
