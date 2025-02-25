def main():
    try:
        fraction = input("Fraction: ").strip()
        x,y = map(int,fraction.split('/'))
        percentage = convert(x,y)
        print(guage(percentage))
    except (ValueError,ZeroDivisionError):
        print("Invalid")

def convert(a,b):
    if b == 0:
        raise ZeroDivisionError
    if a > b:
        raise ValueError
    result = int(round((a/b)* 100))
    return result

def guage(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
# print(guage(1))
if __name__ == "__main__":
    main()