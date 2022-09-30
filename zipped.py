inputt = list(map(int,input().split()))

N = inputt[0]
X = inputt[1]

new = []
for i in range(X):
    new_inputs = list(map(float, input().split()))
    new += [new_inputs]


for i in list(zip(*new)):
    total = 0
    for k in i:
        total += k
    print(total/X)
