#Here are the list of the items available in my vending machine
items = {
    '1D': {'name': 'Pepsi', 'price': 3.00},
    '2D': {'name': 'Mt Dew', 'price': 3.00},
    '3D': {'name': 'Fanta', 'price': 3.00},
    '4D': {'name': 'Coke', 'price': 3.00},
    '5D': {'name': 'Sprite', 'price': 3.00},
    '1S': {'name': 'Doritos', 'price': 7.00},
    '2S': {'name': 'Lays', 'price': 8.00},
    '3S': {'name': 'Cheetos', 'price': 7.00},
    '4S': {'name': 'Pringles', 'price': 9.00},
}

#The machine will display the items with code
def display_items():
    print("|          Vending Machine Items            |")
    print("|    Code    |        Item         | Price  |")
    print("|===========================================|")
    for code, item_info in items.items():
        print(f"| {code:<10} | {item_info['name']:<20} | A{item_info['price']:.2f} |")
    print("|===========================================|")

#My machine will ask you to put the code of the item you want to purchase
def purchase(cart):
    while True:
        code = input("Enter the code of the item you want to add to your cart (or 'x' to finish): ")
        if code.lower() == 'x':
            break

        if code in items:
            item_info = items[code]
            name = item_info['name']
            price = item_info['price']

            print(f"You have added: {name} - A{price:.2f}")
            cart.append((name, price))
        else:
            print("Invalid code. Please select a valid item.")

#If you didnt put any code it will tell you that your cart is empty
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        total_price = sum(item[1] for item in cart)
        print("|          Your Cart         |")
        print("|  Item              Price   |")
        print("|============================|")
        for item, price in cart:
            print(f"| {item:<20} | A{price:.2f} |")
        print("|============================|")
        print(f"Total: A{total_price:.2f}")

def insert_money(cart):
    if not cart:
        print("Your cart is empty. Please add items before inserting money.")
        return

#My machine will ask you to insert money (you can insert exact amount or more, it depends on the user)
    total_price = sum(item[1] for item in cart)
    cash = float(input(f"Insert exact amount {total_price:.2f} or more: "))

    if cash >= total_price:
        return cash
    else:
        print("Insufficient funds. Please insert more cash.")
        return None

#This is the last part, the machine will show you your receipt
def generate_receipt(cart, total_price, cash):
    if not cart:
        print("No items purchased.")
    else:
        print("\n========= Receipt ==========")
        for item, price in cart:
            print(f"{item:<20} A{price:.2f}")
        print("|============================================================================|")
        print(f"Total: A{total_price:.2f}")
        print(f"Cash Inserted: A{cash:.2f}")
        change = cash - total_price
        print(f"Your Change is: A{change:.2f} Thank you for using my machine, Have a great day!")
        print("=============================================================================\n")

#Initialize an empty cart
cart = []

#Display available items
display_items()

#Purchase items and add them to the cart
purchase(cart)

#Display the final cart
display_cart(cart)

#Insert money
cash_inserted = insert_money(cart)
while cash_inserted is None:
    cash_inserted = insert_money(cart)

#Generate and display the receipt
total_price = sum(item[1] for item in cart)
generate_receipt(cart, total_price, cash_inserted)
