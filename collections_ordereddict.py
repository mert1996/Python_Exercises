from collections import OrderedDict

num_items = int(input())
ordered_Dict = OrderedDict()

for i in range(num_items):
    item_price = input().split()
    price = int(item_price[-1])
    item_price.pop(-1)
    
    item_name = ""
    for item in item_price:
        item_name += item + " "
    item_name = item_name.strip()

    if item_name in ordered_Dict:
        ordered_Dict[f"{item_name}"] += price 
    else:
        ordered_Dict[f"{item_name}"] = price

for key,value in ordered_Dict.items():
    print(key,value)

         
