# products.py

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

def show_products():
    for product in products:
        print(f"ID: {product['id']}  Name: {product['name']:^20}  Color: {product['color']:^10}  Size: {product['size']:^6} Price: {product['price']:^10} Toman  Stock: {product['stock']}")

def find_product_by_id(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
