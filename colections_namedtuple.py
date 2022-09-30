from collections import namedtuple

total_students = int(input())
column_names = list(map(str,input().split()))

index = column_names.index("MARKS")

sum = 0
for i in range(total_students):
    inp = input().split()
    sum += int(inp[index])

print(sum/total_students)
