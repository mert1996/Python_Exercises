import numpy as np
np.set_printoptions(legacy="1.13")

N_and_M = list(map(int,input().split()))

N = N_and_M[0]
M = N_and_M[1]

print(np.eye(N,M))
