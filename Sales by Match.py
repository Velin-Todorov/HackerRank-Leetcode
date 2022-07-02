def sockMerchant(n, ar):
    number_of_pairs = 0
    pairs = {}
    for sock in ar:
        if sock not in pairs:
            pairs[sock] = 0
        pairs[sock] += 1

        if pairs[sock] == 2:
            number_of_pairs += 1
            del pairs[sock]
    return number_of_pairs


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
