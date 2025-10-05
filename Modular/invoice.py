# invoice.py
# module part
import datetime
# json part
import json
import os

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
    # json    ## item 
    items = [{"name": item.product['name'], "quantity": item.quantity} for item in cart]
    #
    for item in cart:
        print(f"- {item.product['name']} × {item.quantity}")
    print(f"Amount payable: {total} Toman")
    # json
    invoice_data = {
        "date": now,
        "customer": name,
        "total": total,
        "items": items     ## item    ### tbh output is ugly af but it work so...   
    }
    filename = f"orders_{name}.json"
    #
    try:
        # Load existing invoices if file exists
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                invoices = json.load(f)
        else:
            invoices = []
        # Append new invoice
        invoices.append(invoice_data)
        # Save back to file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(invoices, f, ensure_ascii=False, indent=2)
        print(f"Order saved to file ({filename})")
    except Exception as e:
        print(f"Error saving order: {e}")
    cart.clear()
    

# json ↑
# txt ↓    
#    try:
#        with open(f"orders {name}.txt", "a", encoding="utf-8") as f:
#            f.write(f"{now} | {name} | مبلغ: {total} Toman\n")
#        print("Order saved to file(orders.txt)")
#    except:
#        print("Error saving order.")
#    cart.clear()
