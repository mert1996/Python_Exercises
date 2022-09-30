import numpy as np

N_and_M = list(map(int,input().split()))
N = N_and_M[0]

matrix = []
for rows in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

arr = np.array(matrix)
minimum = np.min(arr,axis=1)
maximum = np.max(minimum)
print(maximum)
