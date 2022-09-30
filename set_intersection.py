eng = int(input())
roll_eng = set(map(int,input().split()))

fre = int(input())
roll_fre = set(map(int,input().split()))

intersec = roll_fre.intersection(roll_eng)

print(len(intersec))
