cube = lambda x: x**3

liste = []
def fibonacci(n):
    for i in range(0,n):
        if i == 0 or i == 1:
            liste.append(i)
        else:
            number = liste[-1]+liste[-2]
            liste.append(number)
    return liste

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

