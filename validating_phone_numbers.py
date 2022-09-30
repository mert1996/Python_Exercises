import re

inputs = int(input())

liste = []
for number in range(inputs):
    phone_number = input()
    pattern = r"^[7-9][0-9]{9}"
    regex = re.findall(pattern, phone_number)
    
    if regex and len(phone_number) == 10:
        liste.append("YES")
    else:
        liste.append("NO")

for i in liste:
    print(i)
