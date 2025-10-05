# invoice.py

import datetime

def display_invoice(cart):
    if cart.is_empty():
        print("The shopping cart is empty.")
        return
    print("\nOrder invoice:")
    total = 0
    for i, item in enumerate(cart, 1):
        name = item.product["name"]
        qty = item.quantity
        price = item.get_total_price()
        total += price
        print(f"{i}. {name} * {qty} = {price} Toman")
    print(f"Total: {total} Toman")

def finalize_order(cart):
    if cart.is_empty():
        print("The shopping cart is empty.")
        return
    name = input("Customer Name: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nFinal invoice registered:")
    print(f"Customer: {name}")
    print(f"Date: {now}")
    total = cart.total()
    for item in cart:
        print(f"- {item.product['name']} × {item.quantity}")
    print(f"Amount payable: {total} Toman")
    try:
        with open(f"orders {name}.txt", "a", encoding="utf-8") as f:
            f.write(f"{now} | {name} | مبلغ: {total} Toman\n")
        print("Order saved to file(orders.txt)")
    except:
        print("Error saving order.")
    cart.clear()
