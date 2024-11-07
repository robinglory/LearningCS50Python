# while True:
#     x = int(input("What is x? "))

#     if x%2 == 0:
#         print("This is even")
#     else:
#         print("This is odd!!")

def main():
    x = int(input("What is the number? "))
    if is_even(x):
        print("This is the even number")
    else: 
        print("This is nothing but odd number! ")

def is_even(n):
    # if n%2 == 0:
    #     return  True

    #we gonna do the elegant way
    # return True if n%2 == 0 else False

    ## now this headache way
    return n % 2  == 0
main()