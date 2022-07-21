def bigSorting(unsorted):
    for i in range(len(unsorted)):
        for j in range(i + 1, len(unsorted)):

            if unsorted[i] >= unsorted[j]:
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]

    result = [str(x) for x in unsorted]
    return result


n = int(input().strip())

unsorted = []

for _ in range(n):
    unsorted_item = int(input())
    unsorted.append(unsorted_item)

print(bigSorting(unsorted))