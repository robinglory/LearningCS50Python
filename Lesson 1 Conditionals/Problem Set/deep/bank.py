greeting = input("Greeting: ").lower().strip()


first_letter = greeting[0]
# print(first_letter)

if greeting.startswith("hello"):
    print("$0");
elif first_letter == "h":
    print("$20")
else:
    print("$100")

