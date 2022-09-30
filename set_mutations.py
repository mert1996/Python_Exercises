set_numb_A = int(input())
set_A = set(map(int, input().split()))

number_sets = int(input())

for i in range(0,number_sets):
    command = input().split()
    if command[0] == "intersection_update":
        new_set = set(map(int, input().split()))
        set_A.intersection_update(new_set)
    if command[0] == "update":
        new_set = set(map(int, input().split()))
        set_A.update(new_set)
    if command[0] == "difference_update":
        new_set = set(map(int, input().split()))
        set_A.difference_update(new_set)
    if command[0] == "symmetric_difference_update":
        new_set = set(map(int, input().split()))
        set_A.symmetric_difference_update(new_set)

sum = 0
for i in set_A:
    sum += i

print(sum)
