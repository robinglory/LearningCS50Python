import random
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Riven Claw"]
    def sort(self,name):
        house = random.choice(self.houses)
        print(f"{name} has been sorted into {house} house!")

def main():
    hat = Hat()
    hat.sort("Harry Potter")

if __name__ == "__main__":
    main()