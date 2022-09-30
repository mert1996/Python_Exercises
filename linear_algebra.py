import numpy as np

N = int(input())

empty_list = []
for rows in range(N):
    row = list(map(float,input().split()))
    empty_list.append(row)

determinant = np.linalg.det(empty_list)

with_two_decimals = round(determinant,2)

print(with_two_decimals)