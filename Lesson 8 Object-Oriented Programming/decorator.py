# class Student:
#     def __init__(self, house):
#         self.house = house  # uses setter

#     @property
#     def house(self):
#         print("Getting the house")
#         return self._house

#     @house.setter
#     def house(self, value):
#         print(f"Trying to set house to '{value}'")
#         if value not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house!")
#         self._house = value

# student = Student("Ravenclaw")     # setter is called
# # print(student.house)               # getter is called
# # student.house = "Shrek House"      # setter raises error!


class ATMCard:
    def __init__(self, pin):
        self.pin = pin
    
    @property
    def pin(self):
        print("Getting the PIN")
        return self.pin
    
    @pin.setter
    def pin(self, new_pin):
        if not new_pin.isdigit():
            raise ValueError("Pins must in digit")
        if len(new_pin) != 4:
            raise ValueError("Must be 4 numbers only")
        self._pin = new_pin

card = ATMCard("1234")     # valid PIN
print(card.pin)     
card = ATMCard("1234")     # valid PIN
print(card.pin)            # prints "1234" using @property

card.pin = "abcd"          # ❌ error: not digits
card.pin = "12"            # ❌ error: too short
card.pin = "5678"          # ✅ valid change
