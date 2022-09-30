import numpy as np

N_and_M = list(map(int,input().split()))
N = N_and_M[0]
M = N_and_M[1]

matrix = []
for rows in range(N):
    row = list(map(int,input().split()))
    matrix.append(row)

arr = np.array(matrix)
sum = np.sum(arr, axis=0)
product = np.prod(sum)
print(product)
