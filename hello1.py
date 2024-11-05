# ##This time we are going to use the function def
# def main():
#     global name;
#     name = input("What is your name?");
#     hello(name)

# def hello(to):
#     print(f"Hello, {to}")

# main();

def main():
    x = int(input("What's x? "))
    print(f"x squared is , {square(x)}")

def square(n):
    return  n*n
main()