# name = input("What is your name? ")
# house = input ("What is your house? ")

# print(f"Hello {name}, you are in {house} house!")

# def main():
#     name = get_name()
#     house = get_house()
#     print(f"Hello {name}, you are in {house} house!")

# def get_name():
#     return input("What is your name? ")
# def get_house():
#     return input("What is your house? ")

# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Riven Claw"

#     print(f"Hello {student[0]} , you are in {student[1]} house! and your parent is {student[2]}")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     parent = input("What is your parent? ")
#     return name, house, parent

# if __name__ == "__main__":
#     main()
# If we type input as Padma, Riven Claw, and Padma's parent is Riven Claw, the output will be: error: 'tuple' object does not support item assignment.
# This is because we are trying to change the value of a tuple, which is immutable.

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Riven Claw"

    print(f"Hello {student[0]}, you are in {student[1]} house! and your parent is {student[2]}")

def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    parent = input("What is your parent? ")
    return [name, house, parent]
if __name__ == "__main__":
    main()
