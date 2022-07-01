n, m = [int(x) for x in input().split()]

grades = [[float(x) for x in input().split()] for i in range(m)]
averages = []

for grade in zip(*grades):
    avg = sum(grade) / len(grade)
    averages.append(avg)

print('\n'.join(str(s) for s in averages))


