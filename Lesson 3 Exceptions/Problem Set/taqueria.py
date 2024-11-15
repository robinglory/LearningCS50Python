def main():
    # Define the menu
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total = 0.0

    while True:
        try:
            # Prompt the user for an item
            item = input("Item: ").title()
            
            # Check if the item exists in the menu
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            # If item is not in the menu, ignore it
            else:
                continue
        except EOFError:
            # Break the loop when user inputs control-d (EOF)
            print()
            break

if __name__ == "__main__":
    main()
