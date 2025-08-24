# simple_kiosk.py

"""
تمرین گروهی اول - سیستم ساده ثبت سفارش لباس
"""

import datetime

# ---------- داده‌های اولیه لباس‌ها ----------
# Part 1
# Mandatory: Reach to 10 rows     |     add 6 more record
# Optional:  add more columns     |     eg: color, size, .etc    
products = [
    {"id": 1, "name": "T-shirt", "color": "white", "size": "M", "price": 150000, "stock": 5},
    {"id": 2, "name": "Jeans", "color": "blue", "size": "32", "price": 350000, "stock": 3},
    {"id": 3, "name": "leather jacket", "color": "brown", "size": "XXXL", "price": 750000, "stock": 2},
    {"id": 4, "name": "Suit shirt", "color": "white", "size": "XXL", "price": 250000, "stock": 4},
    {"id": 5, "name": "Hoodie", "color": "black", "size": "L", "price": 420000, "stock": 6},
    {"id": 6, "name": "Summer dress", "color": "red", "size": "S", "price": 300000, "stock": 4},
    {"id": 7, "name": "Chinos", "color": "khaki", "size": "34", "price": 280000, "stock": 5},
    {"id": 8, "name": "Leather boots", "color": "black", "size": "42", "price": 650000, "stock": 2},
    {"id": 9, "name": "Polo shirt", "color": "navy", "size": "M", "price": 180000, "stock": 7},
    {"id":10, "name": "Cardigan", "color": "gray", "size": "L", "price": 370000, "stock": 3},
]

# ---------- کلاس سبد خرید ----------
class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product["price"] * self.quantity

# ---------- نمایش لیست لباس‌ها ----------
# Part 2
# Fill it
def show_products():
    for product in products:    # < left allign   > right allign    ^ center allign     number ? cell space    # color and size column added    # < shifted to ^
        print(f"ID: {product['id']}  Name: {product['name']:^20}  Color: {product['color']:^10}  Size: {product['size']:^6} Price: {product['price']:^10} Toman  Stock: {product['stock']}")

# ---------- جستجوی کالا براساس ID ----------
# Part 3
# Fill it
def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    

# ---------- اجرای منوی برنامه ----------
# DON'T touch yet ⚠
# تابع هایی که در بخش ۲ و ۳ پر می‌کنید ، ورودی و خروجی ها ش اینجا استفاده میشه
def main():
    cart = []

    while True:
        print("\n --- Main Menu ---")#منوی اصلی
        print("1. Clothes Show")#نمایش لباس ها
        print("2. Add to Cart")#اضافه کردن به سبد خرید
        print("3. Invoice display")#نمایش فاکتوز
        print("4. Finalizing the order")#نهایی سازی فروش 
        print("5. Exit")#خروج

        choice = input(" Your choice: ")#انتخاب شما

        if choice == "1":
            show_products()

        elif choice == "2":
            try:
                product_id = int(input(" Enter the clothing ID: "))# وارد کردن ID لباس: "
                product = find_product_by_id(product_id)
                if not product:
                    print(" No clothes found with this ID.")#لباس با این ایدی پیدا نشد
                    continue
                quantity = int(input(" Desired quantity: "))# تعداد مورد نظر: "
                if quantity <= 0:
                    print("The number must be greater than zero.")# تعداد باید بیشتر از صفر باشد.
                    continue
                if quantity > product["stock"]:
                    print("Not enough inventory.")# موجودی کافی نیست.
                    continue
                product["stock"] -= quantity
                cart.append(CartItem(product, quantity))
                print(" Added to cart.")# به سبد خرید اضافه شد.

            except ValueError:
                print("Please enter only numbers.")# لطفاً فقط عدد وارد کنید.

        elif choice == "3":
            if not cart:
                print(" The shopping cart is empty.")# سبد خرید خالی است.
                continue
            print("\n Order invoice:")#\n🧾 فاکتور سفارش:
            total = 0
            for i, item in enumerate(cart, 1):
                name = item.product["name"]
                qty = item.quantity
                price = item.get_total_price()
                total += price
                print(f"{i}. {name} * {qty} = {price} Toman")
            print(f"Total: {total} Toman")

        elif choice == "4":
            if not cart:
                print("The shopping cart is empty.")
                continue
            name = input("Customer Name: ")# نام مشتری:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("\nFinal invoice registered:")#\n فاکتور نهایی ثبت شد:
            print(f"Customer: {name}")
            print(f"Date: {now}")
            total = 0
            for item in cart:
                print(f"- {item.product['name']} × {item.quantity}")
                total += item.get_total_price()
            print(f"Amount payable: {total} Toman")

            # ذخیره در فایل (فاکتور)
            try:
                with open(f"orders {name}.txt", "a", encoding="utf-8") as f:
                    f.write(f"{now} | {name} | مبلغ: {total} Toman\n")
                print("Order saved to file(orders.txt)")
            except:
                print("Error saving order.")

            cart.clear()

        elif choice == "5":
            print("Goodby!")
            break

        else:
            print("Invalid selection, try again.")

# ---------- اجرای برنامه ----------
if __name__ == "__main__":
    main()




