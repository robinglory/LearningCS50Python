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