eng = int(input())
roll_eng = set(map( int, input().split()))

fre = int(input())
roll_fre = set(map(int, input().split()))

diff = roll_eng.difference(roll_fre)
print(len(diff))
