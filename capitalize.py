def solve(s):
    name = s.split(" ")
    name2 = ""
    for i in name:
        b = i.capitalize()
        name2 += b+" "
    return name2

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)

