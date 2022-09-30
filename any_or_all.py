N = int(input())
numbers = list(map(int, input().split()))

condition = True

for i in numbers:
    string_number = str(i)
    if str(i) == string_number[::-1]:
        condition = True
        break
    else:
        condition = False
        
for i in numbers:
    if i >0:
        pass
    else:
        condition = False



print(condition)
