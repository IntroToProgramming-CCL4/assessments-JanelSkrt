sandwich_orders = ['Cheese Sandwich','Egg Sandwich', 'Grilled Cheese', 'Tuna Sandwich', 'Chicken Sandwich']
finished_sandwiches =[]#this is a empty list

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()#this puts all the sandwich in sandwich_orders inside current_sandwich
    print("\nI made your",current_sandwich)#this prints out that you make the sandwich
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich , " is done\n")