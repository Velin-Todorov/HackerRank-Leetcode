from collections import Counter

def equalizeArray(arr):
    counted = Counter(arr)
    max_val = max(counted.values())

    if max_val <= 1:
        return len(arr) - 1

    unique = {k: v for k, v in counted.items() if v < max_val}
    result = sum(unique.values())

    unique_values = {k: v for k, v in counted.items() if v == max_val}

    if len(unique_values) > 1:
        while len(unique_values) != 1:
            k, v = unique_values.popitem()
            result += v

        return result

    return result


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)