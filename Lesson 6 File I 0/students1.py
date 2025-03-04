import csv
name = input("What is your name? ")
home = input("Where is your home? ")

# with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\students.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open(r"C:\Users\ASUS\Documents\CS50 Python\Lesson 6 File I 0\students2.csv","a",newline="")as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})