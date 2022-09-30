num_test_case = int(input())

for i in range(num_test_case):
    num_elements_A = int(input())
    elements_A = set(map(int,input().split()))
    num_elements_B = int(input())
    elements_B = set(map(int,input().split()))

    if elements_A.issubset(elements_B):
        print(True)
    else:
        print(False)
