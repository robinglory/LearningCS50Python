def main():
    greeting = input("Greeting: ").lower().strip()
    value(greeting)
def value(greeting):
    first_letter = greeting[0]
    if greeting.startswith("hello"):
        print("$0");
    elif first_letter == "h":
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
