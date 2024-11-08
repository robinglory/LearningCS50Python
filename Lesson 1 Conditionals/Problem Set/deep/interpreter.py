def main():
    equation = input("Expression: ")
    x , y, z = equation.split()

    if y == "+":
        print(f"{float(x) + float(z)}")
    elif y == "-":
        print(f"{float(x) - float(z)}")
    elif y == "*":
        print(f"{float(x) * float(z)}")
    elif y == "/":
        print(f"{float(x)/float(z)}")
    else:
        print("I am just a simple math interpreter. Don't bully me!!")
main()