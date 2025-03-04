# with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\students.csv","r") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         print(f"Hello, {name}. You are in {house} house.")
#         # print(row[1])

import csv
students = []

with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\students.csv", "r") as file:
#     for line in file:
#         name,house,home = line.rstrip().split(",")
#         student = {"name": name, "house": house, "home": home}
#         # student = {}
#         # student["name"] = name
#         # student["house"] = house
#         # print(student)
#         students.append(student)
#         # print(students)
# # def get_name(student):
# #     return student["name"]
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"], "home": row["home"]})
        # print(row)
        # print(students)
for student in sorted(students, key = lambda student: student["name"], reverse=False):
    print(f"Hello, {student['name']}. You are in {student['house']} house. You are from {student['home']}.")