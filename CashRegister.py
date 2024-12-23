class CashRegister:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        self.total += price * quantity
        print(f"Added {quantity} x {name} @ ${price:.2f} each. Total: ${self.total:.2f}")

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["price"] * item["quantity"]
                print(f"Removed {item['quantity']} x {name}. Total: ${self.total:.2f}")
                self.items.remove(item)
                return
        print(f"Item '{name}' not found in the cart.")

    def display_items(self):
        if not self.items:
            print("No items in the cart.")
            return
        print("\nItems in the cart:")
        for item in self.items:
            print(f"- {item['quantity']} x {item['name']} @ ${item['price']:.2f} each")
        print(f"\nCurrent total: ${self.total:.2f}")

    def checkout(self):
        if not self.items:
            print("Cart is empty. Nothing to checkout.")
            return
        print("\nFinalizing your purchase...")
        self.display_items()
        print(f"Total due: ${self.total:.2f}")
        payment = float(input("Enter payment amount: $"))
        if payment >= self.total:
            change = payment - self.total
            print(f"Payment accepted. Change: ${change:.2f}. Thank you for shopping!")
            self.items = []
            self.total = 0.0
        else:
            print(f"Insufficient payment. You still owe: ${self.total - payment:.2f}")

if __name__ == "__main__":
    register = CashRegister()
    
    while True:
        print("\n--- Cash Register Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Items")
        print("4. Checkout")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: $"))
            quantity = int(input("Enter quantity: "))
            register.add_item(name, price, quantity)
        elif choice == "2":
            name = input("Enter the name of the item to remove: ")
            register.remove_item(name)
        elif choice == "3":
            register.display_items()
        elif choice == "4":
            register.checkout()
        elif choice == "5":
            print("Exiting the cash register. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
