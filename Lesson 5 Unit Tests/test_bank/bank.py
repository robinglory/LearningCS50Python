def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")  # Format output in main()

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0  # Return int, not f-string
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
