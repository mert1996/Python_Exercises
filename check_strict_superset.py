elements_A = set(map(int, input().split()))
num_sets = int(input())

emp = []
for i in range(num_sets):
    emp.append(set(map(int, input().split())))

true = 0
false = 0

for i in emp:
    if elements_A.issuperset(i):
        true +=1
        print(True)
    else:
        false +=1
        print(False)

if false > 0:
    print(False)
else:
    print(True)
