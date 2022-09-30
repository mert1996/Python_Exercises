eng = int(input())
roll_eng = set(map(int, input().split()))

fre = int(input())
roll_fre = set(map(int, input().split()))

total= roll_eng.union(roll_fre)
print(len(total))
