def main():
    x = int(input("What is your number? "))
    print("Your number squared is ", square(x))

def square(x):
    return x**2

if __name__ == "__main__":
    main()