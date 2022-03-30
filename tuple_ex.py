liste = []
def swap_case(s):
    for i in s:
        if i.islower():
           liste.append(i.upper())
        elif i.isupper():
            liste.append(i.lower())
        else:
            liste.append(i) 

    new = ""
    for i in liste:
        new += i
    return new


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)