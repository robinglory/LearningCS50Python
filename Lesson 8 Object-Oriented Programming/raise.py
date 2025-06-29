# class Student:
#     def __init__ (self, name, house, patronus):
#         if not name:
#             raise ValueError("Name cannot be empty")
#         if not house:
#             raise ValueError("House cannot be empty")
#         if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Riven Claw"]:
#             raise ValueError("Invalid house")
#         if patronus and patronus not in ["Stag", "Otter", "Doe", "Jack Russell Terrier"]:
#             raise ValueError("Invalid Patronus")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"Student(name={self.name}, house={self.house}, patronus={self.patronus})"
    
#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶"
#             case _:
#                 return "🪄"

# def main():
#     Student = get_student()
#     print(Student)
#     print("Expecto Patrnum!")
#     print(Student.charm())

# def get_student():
#     name = input("Enter the student's name: ")
#     house = input("Enter the student's house: ")
#     patronus = input("Enter the student's patronus: ") or None
#     return Student(name, house, patronus)

# if __name__ == "__main__":
#     main()


# # 🎯 Purpose of __str__()
# # The __str__() method is Python’s "how should I display this object as a string?" function.

# # It gets used when you:

# # Use print(student)

# # Use str(student)

# # Format with f"{student}"

# # But not when you manually access the fields yourself (like student.name).
# # ✅ Summary:
# # You write	What happens
# # print(student)	Calls student.__str__()
# # print(student.name)	Just prints the name attribute
# # f"{student}"	Calls __str__()
# # __str__()	Lets you customize how your object looks when printed

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()