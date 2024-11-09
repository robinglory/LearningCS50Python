# def main():
#     print_column(3)


# def print_column(heightt):
#     for _ in range(heightt):
#         print("#")

# main()

# def main():
#     print_row(4)

# def print_row(row):
#     print("?"*row,)

# main()

def main():
    print_square(3)


def print_square(size):

    #for each row in square
    for i in range(size):
        #for each brick in  row
        for j in range(size):
            #Print brick
            print("### ",end = "")
        print("")

main()