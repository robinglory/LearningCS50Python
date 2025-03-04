# name = input("What's your name? ")

# with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\name.txt","a") as file:
#     file.write(f"{name}\n")
#     # file.close

# with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\name.txt","r") as file:
#     for line in file:
#         print(f"Hello, {line.strip()}")
#     lines = file.readlines()

# for line in lines:
#     print(f"Hello, {line.rstrip()}")
##csv == comma seprated value
names = []
with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\name.csv","r") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names,reverse=True):
    if name == "Yan Naing":
        print(f"Hello, {name}. How are you doing?")
        break
    else:
        print("No name found!")
        break