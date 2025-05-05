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

# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Riven Claw"

#     print(f"Hello {student[0]}, you are in {student[1]} house! and your parent is {student[2]}")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     parent = input("What is your parent? ")
#     return [name, house, parent]
# if __name__ == "__main__":
#     main()
#But if we change the tuple to a list, we can change the value of the list.
# This is because lists are mutable, which means we can change their values.


# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Riven Claw"
#     print(f"Hello {student['name']}, you are in {student['house']} house!")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return {
#         "name":name,
#         "house":house
#     }

# if __name__ == "__main__":
#     main()
# #But if we change the list to a dictionary, we can change the value of the dictionary.
# # This is because dictionaries are mutable, which means we can change their values.
# # But if we change the dictionary to a class, we can change the value of the class.
# # This is because classes are mutable, which means we can change their values.

# class Student:
#     def __init__(self,name,house):
#         if not name:
#             raise ValueError("Missing name") 
#         if house not in ["Gryfindor", "Slytherin", "Hufflepuff", "Riven Claw"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
    

# def main():
#     student = get_student()
#     if student.name == "Padma":
#         student.house = "Riven Claw"
#     print(f"Hello {student.name}, you are in {student.house} house!")

# # def get_student():
# #     student = Student()
# #     student.name = input("What is your name? ")
# #     student.house = input("What is your house? ")
# #     return student
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house, patrounus):
#         if not name:
#             raise ValueError("Missing Name")
#         if house not in ["Gryfindor", "Slytherin", "Hufflepuff", "Riven Claw"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.patrounus = patrounus
    
#     def __str__(self):
#         # return f"{self.name} is in {self.house} house and the patrounus is {self.patrounus}"
#         return f"Hello {self.name}, you are in {self.house} house! and your patrounus is {self.patrounus}"

#     # def charm(self):
#     #     match self.patrounus:
#     #         case "Stag":
#     #             return "🦌"
#     #         case "Otter":
#     #             return "🦦"
#     #         case "Hare":
#     #             return "🐇"
#     #         case "Jack Russle Terrier":
#     #             return "🐕"
#     #         case "Phoenix":
#     #             return "🦅"
#     #         case _:
#     #             return "🪄"
# def main():
#     student = get_student()
#     if student.name == "Padma":
#         student.house = "Riven Claw"
#     print(student)
#     print("Expecto Patronum!")
#     print(student.charm())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patrounus  = input("Patrounus: ")
#     return Student(name,house,patrounus)

# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
 
    def __str__(self):
        # return f"{self.name} is in {self.house} house and the patrounus is {self.patrounus}"
        return f"Hello {self.name}, you are in {self.house} house!"
    
    #Getter method for name
    @property
    def name(self):
        return self._name
    #setter method for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("You must Provide a Name!")
        
    ##This is a getter method for the name attribute.
    @property
    def house(self):
        return self._house
    
    ##This is a setter method for the house attribute.
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Riven Claw"]:
            raise ValueError("Invalid House, please choose from Gryffindor, Slytherin, Hufflepuff, or Riven Claw")
        self._house = house

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Riven Claw"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)

if __name__ == "__main__":
    main()

