def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass
        # else:
        #     return x
    #         break
    # return x
    # so in this function, i use else and break to break out the while loop
    #but Now i will show you a much faster way just return the value.
    #Because it acts just like a break (a much stronger break)


main()
