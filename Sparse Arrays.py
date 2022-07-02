from collections import Counter


def matchingStrings(strings, queries):
    counter = Counter(strings)
    result = []
    for query in queries:
        result.append(counter[query])

    return result


if __name__ == '__main__':
    strings_count = int(input().strip())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(res)
