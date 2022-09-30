import numpy as np

N_M_P = list(map(int, input().split()))
N = N_M_P[0]
M = N_M_P[1]
P = N_M_P[2]

empty_column_list = []

for i in range(N):
    columns = list(map(int,input().split()))
    for item in columns:
        empty_column_list.append(item)

first_matrix = np.array(empty_column_list)
first_matrix = first_matrix.reshape(N,P)

second_empty_column_list = []
for i in range(M):
    columns = list(map(int,input().split()))
    for item in columns:
        second_empty_column_list.append(item)

second_matrix = np.array(second_empty_column_list)
second_matrix = second_matrix.reshape(M,P)

print(np.concatenate((first_matrix, second_matrix), axis=0))
