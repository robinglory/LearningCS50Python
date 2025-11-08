# class Person:
#     def __init__(self,name):
#         self.name = name
    
#     def greet(self):
#         return f"Hello, my name is {self.name}."
    
#     def __str__(self):
#         return f"This is the person you have greated called {self.name}"

# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y 
    
#     def __str__(self):
#         pass

#     def sum(self, x, y):
#         return x + y
        
#     def minus(self,x,y):
#         return self.x - self.y
    
# person1 = Person("Yan Naing")
# print(person1)  # Output: Hello, my name is Yan Naing.
# clac = Calculator(3,5)
# # print(clac)
# print(clac.sum(5,3))
# print(clac.minus(8,2))


# class Music:
#     def __init__(self,title,artist):
#         self.title = title
#         self.artist = artist
#     def __str__(self):
#         return f"{self.title} by {self.artist}"
#     def play(self):
#         return f"Playing {self.title} by {self.artist}"

# song = Music("Imagine","John Lennon")
# print(song.play())


# class HappyBirthday:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Happy Birthday {self.name}! You are now {self.age} years old."
    
#     def next_year(self):
#         self.age += 1
#         return f"Next year, you will be {self.age} years old."

# person1 = HappyBirthday("Alice", 30)
# print(person1)
# print(person1.next_year())

# print(person1)
# print(person1.next_year())

#Creating the MP3 Player class
# class MP3Player:
#     def __init__(self, song, artist):
#         self.song = []
#         self.artist = []

#     def __str__(self):
#         return f"This is the implementation of MP3 Player class"
    
#     def add_song(self,song,artist):
#         self.song.append(song)
#         self.artist.append(artist)
#         return f"Added {song} by {artist} to the playlist."
    
#     def del_song(self,song,artist):
#         if song in self.song and artist in self.artist:
#             self.song.remove(song)
#             self.artist.remove(artist)
#             return f"Deleted {song} by {artist} from the playlist."
#         else:
#             return f"{song} by {artist} not found in the playlist."
    
#     def play_song(self,song,artist):
#         if song in self.song and artist in self.artist:
#             return f"Playing {song} by {artist}."
#         else:
#             return f"{song} by {artist} not found in the playlist."
    
#     def show_playlist(self):
#         playlist = []
#         for s, a in zip(self.song, self.artist):
#             playlist.append(f"{s} by {a}")
#         return playlist

# my_player = MP3Player([],[])
# print(my_player.add_song("One love","Bob Marley"))
# print(my_player.play_song("Poker Face","Lady Gaga"))
# print(my_player.add_song("Blinding Lights","The Weeknd"))
# print(my_player.del_song("One love","Bob Marley"))
# print(my_player.play_song("Blinding Lights","The Weeknd"))
# print(my_player.show_playlist())

## Inheritance Example
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def printname(self):
#         return f"This person name is nothing but this '{self.first_name} {self.last_name}' "

# class Student(Person):
#     def __init__(self, first_name, last_name, graduation_year):
#         # Person.__init__(self, first_name, last_name)
#         super().__init__(first_name, last_name)
#         self.graduation_year = graduation_year

#     def welcome(self):
#         return f"Welcome {self.first_name} {self.last_name} to the class of {self.graduation_year}"  

# person1 = Person("John", "Doe")
# print(person1.printname())
# x = Student("Jane", "Doe", 2025)
# print(x.printname())
# print(x.welcome())

## Polymorphism Example
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def speak(self):
#         return "Meow!"

# class Monkey:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
    
#     def speak(self):
#         return "Ooh Ooh Aah Aah!"

# dog = Dog("Buddy", "Golden Retriever")
# cat = Cat("Whiskers", "Siamese")
# monkey = Monkey("George", "Capuchin")

# for x in (dog, cat, monkey):
#     print(f"{x.name} says {x.speak()}")
        

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#     print(f"{x.brand} {x.model}:", end=" ")
#     x.move()

## Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 18:
            self.__age = age
            return f"Age updated to {age} and you are eligible."
        else:
            return "Age must be at least 18."
        
    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.__age})"
    
p1  = Person("Emily", "19")
print(p1.name)      # Accessing public attribute
print(p1.get_age()) # Accessing private attribute via getter
print(p1) # Trying to set age to 17


## Pythonic way
class Person:
    def __init__(self, name, age, job):
        self.name = name  
        self.age = age
        self._job = job
    
    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self, job):
        if job in ["Engineer", "Doctor", "Artist"]:
            self._job = job
            return f"Job updated to {job}."
        else:
            raise ValueError("Invalid job. Choose from Engineer, Doctor, or Artist.")

p2 =  Person("David", 25, "Engineer")
print(p2.job)  # Accessing job via property
p2.job = "Teacher"  # Trying to set an invalid job
print(p2.job)


