# try:
#     x = int(input("What is x?"))
# except ValueError:
#     print("X must be an integer")
# else:
#     print(f"x is nothing but this {x}")

# while True:
#     try:
#         x = int(input("What is x "))
#     except ValueError:
#         print("X is nothing but integer")
#     else:
#         break
# print(f"x is {x}")

def main():
    x = get_x()
    print(f"x is {x}")

def get_x():
    while True:
        try:
            x = int(input("What is the value of x? "))
        except ValueError:
            # print("Please enter only integer!!")
            pass
        else:
            break
    return x

main()