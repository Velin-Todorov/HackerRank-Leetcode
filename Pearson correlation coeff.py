import numpy as np

n = int(input())
A = np.array([float(x) for x in input().split()], int)
B = np.array([float(x) for x in input().split()], int)

print(np.corrcoef(A, B)[0][1])

