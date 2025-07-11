products = {
    "Laptop": 85000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 15000
}

def add_product(name, price):
    if name in products:
        print(f"{name} already exists.")
    else:
        products[name] = price
        print(f"{name} added with price {price}.")

def update_price(name, new_price):
    if name in products:
        products[name] = new_price
        print(f"Price of {name} updated to {new_price}.")
    else:
        print(f"{name} not found in product list.")

def find_in_range(min_price, max_price):
    print(f"Products between Rs. {min_price} and Rs. {max_price}:")
    found = False
    for name, price in products.items():
        if min_price <= price <= max_price:
            print(f"{name}: Rs. {price}")
            found = True
    if not found:
        print("No products found in this price range.")

# Example Usage
add_product("Tablet", 25000)
update_price("Mouse", 700)
find_in_range(1000, 20000)
