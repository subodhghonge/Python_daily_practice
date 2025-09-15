#Shopping Cart
# Concepts Used: list operations (append, remove, in, loops, menus).

# Problem Statement:

# Create a shopping cart where user can add, remove, and view items.
def shopping_card():
    cart = []

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            item = input("Enter item to add: ")
            cart.append(item)
            print(f"{item} added to cart succesfully!")
        elif ch == 2:
            item = input("Enter the item to remove from cart: ")
            if item in cart:
                cart.remove(item)
            else:
                print("Item not found in cart")
            print(f"{item} removed from cart succesfully!")
        elif ch == 3:
            print(f"Cart items {cart}")
        elif ch == 4:
            print("Exiting......Thaank you!")
            break
        else:
            print("Enter a valid number")

shopping_card()