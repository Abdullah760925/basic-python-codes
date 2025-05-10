# grocery_billing_system.py

cart = []

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter price: ₹"))
    quantity = int(input("Enter quantity: "))
    
    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    cart.append(item)
    print("✅ Item added to cart.\n")

def view_cart():
    if not cart:
        print("🛒 Cart is empty!\n")
        return

    print("\nItems in Cart:")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} - ₹{item['price']} x {item['quantity']}")
    print()

def calculate_total():
    total = sum(item['price'] * item['quantity'] for item in cart)
    print(f"🧾 Total Amount: ₹{total:.2f}\n")

def main():
    while True:
        print("==== Grocery Billing System ====")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Calculate Total")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Thank you for shopping! 🛍️")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

main()
