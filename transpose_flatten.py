import numpy as np

dim = list(map(int,input().split()))

rows    = dim[0]
columns = dim[1]

empty_list = []
for i in range(rows):
    lines = list(map(int,input().split()))
    for item in lines:
        empty_list.append(item)

arr = np.array(empty_list)
transpose_arr = arr.reshape(rows,columns)
flatten_arr = arr.flatten()
print(np.transpose(transpose_arr))
print(flatten_arr)