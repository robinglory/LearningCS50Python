#Ask user for their name
name = input("What is your Name?").strip().title()


#Split User's name into first name and last name
first, second, third, fourth = name.split(" ");  #i want to split the sentence in " "


#Say Hello to the user
print(f"Hello, {first + second}");
print(f"So, your family name is {third + fourth}")