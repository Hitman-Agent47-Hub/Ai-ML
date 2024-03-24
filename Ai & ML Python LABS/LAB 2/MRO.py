# Pyhon classes & Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
# Initiate a custom object
person_1 = Person("Alice",20)

print("Name: ",person_1.name," age: ", person_1.age)

# Instance Methods

class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self):
        return (f"{self.name} says woof!")
    
dog_1 = Dog("PitBUll")
print(dog_1.bark())

# Parent class vs Child class

class Animals:
    def speak(self):
        raise NotImplementedError ("Subclass must implement abstract method")
                
class Dog(Animals):
    def speak(self):
        return "Woof!"
    
animal_1 = Dog()
print(animal_1.speak())
# Inheritance & Multiple Inheritance

class Animal:
    def make_sound():
        pass
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound():
        return "Meow!"
    
class DogCat(Dog,Cat):
    pass

pet  = DogCat()
print(pet.make_sound())

# Abstract Classes & Methods
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
    
class Car(Vehicle):
    def move(self):
        return "Car is Moving"
    
# ------------------------------Method Resolution Order(MRO)--------------------------------

class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return "B"
    
class C(A):
    def process(self):
        return "C"
    
class D(B,C):
        pass
    
print(D().process())

# ------------------------------------Practice Exercise-------------------------------------

# Class for Rectangle with length and width, and a method to calculate its area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Calculate area of the rectangle
        return self.length * self.width

R1 = Rectangle(5.5,4.5)
print(R1.area())

# Class for Square that inherits from Rectangle
class Square(Rectangle):
    def area(self):  # Override the area method to calculate area of square
        return self.length ** 2

S1 = Square(5.5,2)
print(S1.area())
# Abstract class for Shape with an abstract method area
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):  # Abstract method to calculate area
        pass


# Concrete class for Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Calculate area of the circle
        return 3.14 * (self.radius ** 2)

C1 = Circle(3.59)
print (C1.area())

# Concrete class for Triangle that inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):  # Calculate area of the triangle
        return 0.5 * self.base * self.height
    
T1 = Triangle(5.5,4.5)
print(T1.area())
        
    
        
