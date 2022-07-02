def hourglassSum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for row in range(len(arr) - 2):
        for col in range(len(arr[row]) - 2):
            current_sum = arr[row][col] + arr[row][col + 1] + arr[row][col + 2] + arr[row + 1][col + 1] \
                          + arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
