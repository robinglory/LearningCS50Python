def main():
    grocery_list = {}

    while True:
        try:
            # Prompt user for an item
            item = input().strip().upper()
            
            # Add the item to the dictionary, counting occurrences
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            # Break the loop when Control-D is pressed
            print()
            break

    # Sort and display the grocery list
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()
