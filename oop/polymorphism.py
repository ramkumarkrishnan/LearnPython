# Polymorphism
print("\nPolymorphic Shapes")

class Shape():
    def __init__(self):
        self.sides = sides

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def getVolume(self):
        pass

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return 3.142 * self.radius ** 2

    def getPerimeter(self):
        return 2 * 3.142 * self.radius

    def getCircumference(self):
        return self.getPerimeter()

shapes = [Rectangle(6, 10), Circle(7)]
print("Sides of a rectangle are", str(shapes[0].sides))
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Perimeter of rectangle is:", str(shapes[0].getPerimeter()))

print("Sides of a circle are", str(shapes[1].sides))
print("Area of circle is:", str(shapes[1].getArea()))
print("Perimeter of circle is:", str(shapes[0].getPerimeter()))

print ("\nOverloading Built-in Operators")

class Complx:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, operand2):  # overloading the `+` operator
        return Complx(self.real + operand2.real, self.imag + operand2.imag)

    def __sub__(self, operand2):  # overloading the `-` operator
        return Complx(self.real - operand2.real, self.imag - operand2.imag)

res = Complx(3, 7) + Complx(2, 5)
print("Result: " + str(res.real) + " + " + str(res.imag) + "j")

print ("\nDuck Typing - polymorphism without inheritance")
x = 5
print (type(x))
x = "String"
print (type(x))

print ("\nCurrency example")

class Fr:
    def Currency(self):
        print ("Euro")

class Jp:
    def Currency(self):
        print ("Yen")

class Ch:
    def Currency(self):
        print ("Renminbi")

class Money:
    def Currency(self, country):
        country.Currency()
    # Currency method must be available in the country object passed in
    # The method name in Money need not be Currency - can be anything
        

m = Money()
fr = Fr()
jp = Jp()
ch = Ch()
m.Currency(fr) # currency is determined at this call. It does not matter
m.Currency(jp) # what object we pass in - as long as the class contains
m.Currency(ch) # the Currency method.

print ("\nAbstract Base Class")

class Shape():
    # Note - in abstract class, there is no class __init__ function
    
    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def getVolume(self):
        pass

class Square(Shape):
    def __init__(self, length=0):
        self.length = length
        self.sides = 4

    def getArea(self):
        return self.length ** 2

    def getPerimeter(self):
        return 4 * self.length

s1 = Shape() # abstract class
s2 = Square(4) # square with length of side=4

print ("\nAbstract Class with abstract method")
print ("\nThis won't compile because Shape has abstract methods")
print ("without method definitions in it")

from abc import ABC, abstractmethod

class Shape(ABC):  # child class of ABC
    #@abstractmethod
    def area (self):
        pass

    #@abstractmethod
    def perimeter (self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4

#s1 = Shape()
#s1 = Square(4)
#print ("Area: ", s1.area)

print ("\nQuiz")
class Parent:
    def prn(self):
        print ("Parent")

class Child(Parent):
    def __init__(self):
        self.a = Parent()
    def prn (self):
        print ("Child")

temp = Child()
temp.a.prn()

print ("\nMethod override using super()")

class Shape():
    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name

class XShape(Shape):
    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return (super().getName() + ". " + self.name)

c1 = XShape("Circle")
print (c1.getName())

print ("\nAnimal Kingdom Test")
class Animal():
    def __init__(self, name=None, sound=None):
        self.name = name
        self.sound = sound

    def Details(self):
        print (self.name)
        print (self.sound)

class Dog(Animal):
    def __init__(self, name=None, sound=None, family=None):
        super().__init__(name, sound)
        self.family = family

    def Details(self):
        super().Details()        
        print (self.family)

class Sheep(Animal):
    def __init__(self, name=None, sound=None, color=None):
        super().__init__(name, sound)
        self.color = color

    def Details(self):
        super().Details()      
        print (self.color)

d1 = Dog("Roscoe", "Woof", "Husky")
d1.Details()
s1 = Sheep("Tanner", "Baa Baa", "Mary")
s1.Details()
