# main.py

from products import products, show_products, find_product_by_id
from cart import Cart
from invoice import display_invoice, finalize_order

def main():
    cart = Cart()
    while True:
        print("\n --- Main Menu ---")
        print("1. Clothes Show")
        print("2. Add to Cart")
        print("3. Invoice display")
        print("4. Finalizing the order")
        print("5. Exit")

        choice = input(" Your choice: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            try:
                product_id = int(input(" Enter the clothing ID: "))
                product = find_product_by_id(product_id)
                if not product:
                    print(" No clothes found with this ID.")
                    continue
                quantity = int(input(" Desired quantity: "))
                if quantity <= 0:
                    print("The number must be greater than zero.")
                    continue
                if quantity > product["stock"]:
                    print("Not enough inventory.")
                    continue
                product["stock"] -= quantity
                cart.add_item(product, quantity)
                print(" Added to cart.")
            except ValueError:
                print("Please enter only numbers.")

        elif choice == "3":
            display_invoice(cart)

        elif choice == "4":
            finalize_order(cart)

        elif choice == "5":
            print("Goodby!")
            break

        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()
