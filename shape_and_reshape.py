import numpy as np

given = list(map(int,input().split()))

arr = np.array(given)
print(arr.reshape([3,3]))
