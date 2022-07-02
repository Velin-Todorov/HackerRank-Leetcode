from collections import deque


def rotateLeft(d, arr):
    arr = deque(arr)

    for _ in range(d):
        x = arr.popleft()
        arr.append(x)

    return ' '.join(str(s) for s in arr)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(d, arr)
    print(result)