def average(array):
    a = set(array)
    sum = 0
    for i in a:
        sum += i
    return sum / len(a)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
