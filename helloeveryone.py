#This is just testing comment.!
#This program is used for asking  name!
# name = input("What is your name??")
# print("Hello,", name , ", Nice to meet you!", sep = '????', end='')
# print("What tf is going on here!!")

# name = input("What is your name?")
# name = name.strip().title() #Remove whitespace from string ##Trying to capatalize the user name!

name = input("What is your name?").strip().title()
# name = name.strip().title() #Remove whitespace from string ##Trying to capatalize the user name!

#splitting the  name

first, last = name.split(" ")
print(f"Hello, {first}")
# print('Hello, i am using the "double quotes"');
# print("Hello, this is using the blackslash \"Friend\"")


