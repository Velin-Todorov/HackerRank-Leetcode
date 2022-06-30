def miniMaxSum(arr):
    sums = []

    for i in range(len(arr)):
        sums.append(sum(arr) - arr[i])

    max_sums = max(sums)
    min_sums = min(sums)
    return min_sums, max_sums


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(*miniMaxSum(arr))
