eng = int(input())
roll_eng = set(map(int, input().split()))

fre = int(input())
roll_fre = set(map(int, input().split()))

sym_dif = roll_eng.symmetric_difference(roll_fre)
print(len(sym_dif))
