import datetime

inputt = list(map(int,input().split()))

month = int(inputt[0])
day = int(inputt[1])
year = int(inputt[2])

which_Day = datetime.datetime(year,month,day)
which_Day= which_Day.strftime("%A")

which_Day= which_Day.upper()

print(which_Day)
