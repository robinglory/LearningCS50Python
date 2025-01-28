import inflect

def main():
    p = inflect.engine()
    user_names = []

    print("Enter your name: ")
    try:
        while True:
            user_name = input("Input: ")
            user_names.append(user_name)
    except EOFError as e:
        print(e)
    
    format_name = p.join(user_names)
    print(f"Adieu, adieu to {format_name}")

main()