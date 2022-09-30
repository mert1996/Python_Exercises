import re

string = input()

pattern = r"[aeouiAEOUI]{2,}[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]{1}"

answer = re.findall(pattern, string)

if answer:
    for i in answer:
        print(i[:-1])
else:
    print(-1)
