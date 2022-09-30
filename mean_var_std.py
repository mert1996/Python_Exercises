import numpy as np

N_and_M = list(map(int,input().split()))
N = N_and_M[0]

matrix = []
for rows in range(N):
    row = list(map(float,input().split()))
    matrix.append(row)

arr = np.array(matrix)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(np.std(arr))