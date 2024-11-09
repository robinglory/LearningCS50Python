#this is list
# students = ["Hermoine", "Harry", "Ron"]
# houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]


# 
#we are creating the student a new variable to iterate the lists

#you don't really need to declare the student varable at all.
# for student in students:
#     print(student)

#we are using len as a lenght of the students lists.

# for i in range(len(students)):
#     print(i + 1,students[i])

#This is Dictionary
# students = {
#     "Hermoine":"Gryffindor", 
#     "Harry":"Gryffindor",
#     "Ron":"Gryffindor",
#     "Draco":"Slytherin"}

# # print(students["Hermoine"])
# # print(students["Harry"])
# # print(students["Draco"])

# for student in students:
#     print(student, students[student], sep= ", ")

## Now it is time to combine lists with dictionary

students = [
    {"name":"Hermione", "house": "Gryffindor", "patrous": "Otter"},
    {"name":"Harry", "house": "Gryffindor", "patrous": "Stag"},
    {"name":"Ron", "house": "Gryffindor", "patrous": "Jack Russell terrier"},
    {"name":"Draco", "house": "Slytherin", "patrous": None}
]

for student  in students:
    print(student["patrous"], student["house"], sep=", ")