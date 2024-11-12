##While Loop
#  i = 10
# while i != 0 :
#     print("meow")
#     i -= 1 #in javascript or  c++, we use -- but in python we use +=

##For Loop
# for i in [0,1,2]: #[0,1,2]  this is list we use square brackets
#     print("meow")

# ##instead of list we can use range function for the extreme cases
# for i in range(100):
#     print("meow meow")

# for _ in range(6): #When i is not that important we can use _
#     print("meow meow")

# print("meow\n" *3, end ="") ##this is using \n escape key, end key is use
#                             ## to delete the last enter


#To ask the user the valid answer!!
# while True:
#     n = int(input("Whant is n?: "))
#     if n>0:
#         break

# for _ in range(n):
#     print("meow")

#Now we gonna use main()
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What is the number: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()