class Person:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}."
    
    def __str__(self):
        return f"This is the person you have greated called {self.name}"

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __str__(self):
        pass

    def sum(self, x, y):
        return x + y
        
    def minus(self,x,y):
        return self.x - self.y
    
person1 = Person("Yan Naing")
print(person1)  # Output: Hello, my name is Yan Naing.
clac = Calculator(3,5)
# print(clac)
print(clac.sum(5,3))
print(clac.minus(8,2))

