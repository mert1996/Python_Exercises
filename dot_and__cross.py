import numpy as np

N_and_M = list(map(int,input().split()))
N = N_and_M[0]

matrix_A = []
for rows in range(N):
    row = list(map(int,input().split()))
    matrix_A.append(row)

arr_A = np.array(matrix_A)

matrix_B = []
for rows in range(N):
    row = list(map(int,input().split()))
    matrix_B.append(row)

arr_B = np.array(matrix_B)

print(np.cross(arr_A,arr_B))