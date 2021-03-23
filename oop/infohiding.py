# Python OOP - Information Hiding

print ("\nRectangle encapsulation")
class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = length
        self.__width = width

    def setLength(self, length=0):
        self.__length = length
    def setWidth(self, width=0):
        self.__width = width
        
    def getLength(self):
        return self.__length
    def getWidth(self):
        return self.__width
    def getArea(self):
        return self.__length * self.__width
    def getPerimeter(self):
        return 2 * (self.__length + self.__width)

l1 = Rectangle(4, 5)
print (l1.getArea())
l1.setLength(40)
l1.setWidth(50)
print (l1.getLength())
print (l1.getWidth())
print (l1.getArea())
print (l1.getPerimeter())

print ("\nStudent encapsulation")
class Student:
    # class attribute
    maxScore = 100

    def __init__(self, name=None, rollNumber=None, phy=0, chem=0, bio=0):
        self.name = name
        self.__rollNumber = rollNumber
        self.__phy = phy
        self.__chem = chem
        self.__bio = bio

    def setPhy(self, phy=0):
        self.__phy = phy
    def setChem(self, chem=0):
        self.__chem = chem
    def setChem(self, bio=0):
        self.__bio = bio

    def getRollNumber (self):
        return self.__rollNumber
    def getTotalScore (self):
        return (self.__phy + self.__chem + self.__bio)
    def getPercentScore (self):
        return ((self.getTotalScore()/(self.maxScore * 3)) * 100)

s1 = Student("Steve", 12345, 60, 70, 80)
print (s1.getRollNumber())
print (s1.getTotalScore())
print (s1.getPercentScore())

print ("\nPunted Abstraction - I Will Be Back")
