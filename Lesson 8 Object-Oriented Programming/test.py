# name = input("What is your name?")
# age = input("What is your age")
# print(f"Hello {name}, you are {age} years old.")
## This is using just procedural programming and nothing special about it.
##_______________________________________________________________________

##This is time I will use Object-Oriented Programming to do the same thing.
# def main():
#     name = get_name()
#     age = get_age()
#     print(f"Hello {name}, you are {age} years old.")

# def get_name():
#     return input("What is your name? ")

# def get_age():
#     return input("What is your age? ")

# if __name__ == "__main__":
#     main()
# This is a simple program that uses functions to get user input and print a message.
# It demonstrates the use of functions to organize code and make it more readable.
##_______________________________________________________________________

##Using Tuples
# def main():
#     person = get_person()
#     print(f"Hello {person[0]}, you are {person[1]} years old.")
# def get_person():
#     name = input("What is your name? ")
#     age = int(input("What is your age? "))
#     return (name, age)  # Returning a tuple with name and age
# if __name__ == "__main__":
#     main()
## This time i will not use multiple functions, but instead use a single function called get_person and it will return
## a tuple with name and age. This is a simple program that uses tuples to store multiple values in a single variable.
## It demonstrates the use of tuples to group related data together.
##_______________________________________________________________________

##Using Lists
# def main():
#     person = get_person()
#     print(f"Hello {person[0]}, you are {person[1]} years old.")
#     if person[1] < 18:
#         person[1] = 100
#     print(f"Hello {person[0]}, you are now {person[1]} years old after modification.")
# def get_person():
#     name = input("What is your name? ")
#     age = int(input("What is your age? "))
#     return [name, age]  # Returning a list with name and age
# if __name__ == "__main__":
#     main()
## This is the same program as before, but this time I will use a list to store the name and age.
## It demonstrates the use of lists to store multiple values in a single variable and modify them. Mean Lists are mutable
## and can be changed after they are created.
##_______________________________________________________________________

##Using Dictionaries
def main():
    person = get_person()
    print(f"Hello {person['name']}, you are {person['age']} years old.")
def get_person():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    return {'name': name, 'age': age}  # Returning a dictionary with name and age
if __name__ == "__main__":
    main()
## This is the same program as before, but this time I will use a dictionary to store the name and age.
## It demonstrates the use of dictionaries to store key-value pairs, allowing for more descriptive data handling.
## Dictionaries are useful when you want to associate values with specific keys, making the code more readable and maintainable.
##_______________________________________________________________________

