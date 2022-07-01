from collections import Counter

n = int(input())
words = [input() for x in range(n)]

words_counter = Counter(words)


print(len(words_counter))
for x in words_counter.values():
    print(x, end=' ')
