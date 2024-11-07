name = input("What is your name?")

# if name == "Harry" or name == "Hermoine" or name == "Ron":
#     print("Gryffindor")
# else: 
#     print("Who?")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermoine":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who!? ")

match name:
    case "Harry" | "Hermonie" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who!? ")