if __name__ == '__main__':
    s = input()      
    
for i in s:
    if i.isalnum():
        a = True
        break
    else:
        a = False
print(a)

for i in s:
    if i.isalpha():
        a = True
        break
    else:
        a = False
print(a)

for i in s:
    if i.isdigit():
        a = True
        break
    else:
        a = False
print(a)

for i in s:
    if i.islower():
        a = True
        break
    else:
        a = False
print(a)

for i in s:
    if i.isupper():
        a = True
        break
    else:
        a = False
print(a)
