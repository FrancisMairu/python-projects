#inventory system
def add_item(inventory, name, quantity):
    if name in inventory:
        # If it exists, increase the quantity
        inventory[name] += quantity
    else:
        # If it doesn't exist, add it to the inventory
        inventory[name] = quantity
    print(f"Added {quantity} {name}(s) to the inventory.")

def get_item_info(inventory, name):
    # Check if the item exists in the inventory
    if name in inventory:
        # If it exists, print its quantity
        print(f"{name}: {inventory[name]}")
    else:
        # If it doesn't exist, inform the user
        print(f"{name} is not in the inventory.")

def calculate_total_quantity(inventory):
    # Sum up all quantities in the inventory
    return sum(inventory.values())

def main():
    inventory = {}
# Display menu options
    while True:
        
        print("\n1. Add item")
        print("2. Get item information")
        print("3. Display total quantity")
        print("4. Exit")

        # Get user's choice
        choice = input("Enter your choice (1-4): ")

        # Add item to inventory
        if choice == '1':
            
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, name, quantity)
# Get information about a specific item
        elif choice == '2':
            name = input("Enter item name: ")
            get_item_info(inventory, name)
# Calculate and display total quantity of all items
        elif choice == '3':
            total = calculate_total_quantity(inventory)
            print(f"Total quantity of all items: {total}")
# Exit the program
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()