name = input("What is your name? ").strip()
# print(f"Hello, {name}")

if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")