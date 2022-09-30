from itertools import product

A = set(map(int,input().split()))
B = set(map(int,input().split()))

prod = list(product(A,B))

print(*prod)
