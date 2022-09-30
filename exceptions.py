num_test_case = int(input())

for i in range(num_test_case):
    a_and_b = input().split()
    a = a_and_b[0]
    b = a_and_b[1]
    
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")

    except ValueError as a:
        print("Error Code: ",a)
