M = int(input())
setM =  set(map(int, input().split()))

N = int(input())
setN =  set(map(int, input().split()))

dif_M = setM.difference(setN)
print("dif_M : ",dif_M)
dif_N = setN.difference(setM)
print("dif_N : ",dif_N)
new_set = dif_M.union(dif_N)
