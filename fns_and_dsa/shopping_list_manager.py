def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(list):
    item = input("Enter Item you wish to add. ")
    list.append(item)
    
def remove_item(list):
    item = input("Enter Item you wish to remove. ")
    if item in list:
        list.remove(item)
    else:
        print("Item is not in your shopping list")

def view_list(list):
    for item in list:
        print(item)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item(shopping_list)
        elif choice == '2':
            # Prompt for and remove an item
            remove_item(shopping_list)
        elif choice == '3':
            # Display the shopping list
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()