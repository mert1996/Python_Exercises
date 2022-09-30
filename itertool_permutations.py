from cmath import pi
from itertools import permutations

string = input().split()
perm = list(permutations(str(string[0]),int(string[1])))

empty = []
for i in perm:
    o = ""
    for k in i:  
        o+=k
    empty.append(o)

empty.sort()

for i in empty:
   print(i)
