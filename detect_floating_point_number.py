import re

integer = int(input())

list = []
for i in range(integer):
    number = input()
    pattern = r"^[+|-]{0,1}[0-9]{0,}[\.][0-9]{1,}$"
    
    if re.findall(pattern,number):
        print(True)
    else:
        print(False)
