print ("Pastrami is out of stock")
sandwich_orders = ['Cheese Sandwich', 'Pastrami','Egg Sandwich','Grilled Cheese', 'Tuna Sandwich', 'Chicken Sandwich']
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
finished_sandwiches =[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("\nI made your",current_sandwich)
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich , " is done\n")