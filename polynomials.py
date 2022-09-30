import numpy as np

coeff = list(map(float, (input().split())))
value = int(input())

calculation = np.polyval(coeff,value)

print(calculation)