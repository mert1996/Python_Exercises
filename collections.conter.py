from collections import Counter

num_shoes = int(input())
sizes = list(map(int,input().split()))
num_cus = int(input())

counts = Counter(sizes)
total_price = 0

for i in range(1,num_cus+1):
    cust_demand = tuple(map(int,input().split()))
    cust_size = cust_demand[0]
    price = cust_demand[1]

    request = (cust_size)
    try:
        sizes.remove(request)
        total_price += price
    except:
        pass
    

print(total_price)

