def getMoneySpent(keyboards, drives, b):
    max_difference = float('-inf')
    current_difference = 0
    max_difference_list = []

    for i in keyboards:
        current_difference = 0
        for j in drives:
            current_difference = i + j
            if max_difference < current_difference <= b:
                max_difference = current_difference
                max_difference_list.append(max_difference)
            current_difference = 0

    if len(max_difference) > 1:
        return max(max_difference)
    return -1

bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

print(getMoneySpent(keyboards, drives, b))