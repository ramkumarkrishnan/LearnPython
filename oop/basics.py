# Classes and Objects - Basics
print ("Basic Class")
class MyClass:
    pass

obj = MyClass() # creating a MyClass object
print (obj)

print ("\nEmployee Class")
class Employee:
    Id = None
    salary = None
    department = None # compile errors without None

Steve = Employee()

print ("\nProperty outside the Class - Instance variable")
Steve.title = "Manager" # Title not present in Employee

print ("Steve ID: " + str(Steve.Id))
print ("Steve Salary: " + str(Steve.salary))
print ("Steve Dept: " + str(Steve.department))
print ("Steve Title: " + str(Steve.title))

print ("\nClass Initializer - enables creation with default attributes")

print ("\nEmployee Class with __initializer__")
class Employee:
    def __init__(self, Id=None, salary=0, department=None):
        self.Id = Id
        self.salary = salary
        self.department = department # compile errors without None

Steve = Employee(2001, 20001, "Space Odyssey")

print ("Steve ID: " + str(Steve.Id))
print ("Steve Salary: " + str(Steve.salary))
print ("Steve Dept: " + str(Steve.department))

Jobs = Employee()

print ("Jobs ID: " + str(Jobs.Id))
print ("Jobs Salary: " + str(Jobs.salary))
print ("Jobs Dept: " + str(Jobs.department))

class Player:
    teamName = "Liverpool"
    def __init__(self, name=None):
        self.name = name
        self.formerteams = []

p1 = Player("Mo Salah")
p1.formerteams.append('Al Mokawlooon') # append takes only one argument
p1.formerteams.append('Basel')
p1.formerteams.append('Chelsea')
p1.formerteams.append('Fiorentina')
p1.formerteams.append('Roma')
print (p1)
print ("Player: ", p1.name)
print ("Previously with: ", p1.formerteams)

print ("\nPlayer Class with instance, class, static methods, private attributes, private methods")
class Player:
    # class attribute
    teamName = "Liverpool"

    @classmethod
    def getTeamName(cls):
        return cls.teamName

    @staticmethod
    def getRecentNews(source):
        if (source == "Twitter"):
            print ("News from Twitter")
        
    def __init__(self, name=None, level=None, formerteams=[]):
        self.name = name
        self.level = level # Starting XI, Division 1, Division 2
        self.formerteams = formerteams
        self.__salary = 0
        self.__incentives = 0
        self.matches = 0
        self.goals = 0
        self.assists = 0

    # private method
    def __getTax(self, country="UK"):
        if (country == "UK"):
            return (self.__salary * 0.33)
        elif (country == "Spain"):
            return (self.__salary * 0.44)
        elif (country == "Germany"):
            return (self.__salary * 0.35)
        elif (country == "France"):
            return (self.__salary * 0.43)
        elif (country == "Italy"):
            return (self.__salary * 0.38)

    def __putIncentives(self, incentives=0):
        self.__incentives = incentives
        
    # public method
    def putSalary(self, salary=0):
        self.__salary = salary
        
    def getSalary(self):
        self.__putIncentives(15)
        self.__salary += self.__incentives
        return (self.__salary)

tlist = ['Al Mokawlooon','Basel','Chelsea','Fiorentina','Roma']
p1 = Player("Mo Salah", "Starting XI", tlist)
p1.matches = 28
p1.goals = 17
p1.assists = 3
p1.putSalary(55)
print (p1)
print ("Player: " + p1.name + " Matches: " + str(p1.matches) + " Goals: " + str(p1.goals) + " Assists: " + str(p1.assists))
print (Player.getTeamName())
print ("Salary (M): ", p1.getSalary())
print (Player.getRecentNews("Twitter"))
print ("Previous teams: ", p1.formerteams)
print ("Backdoor to Salary: ", p1._Player__salary)
# The following will fail: "Player has no attribute .."
# p1.__putIncentives(15)
# p1.__getTax("Italy")

# Backdoor to private method
p1._Player__putIncentives(15)
print ("Backdoor to Tax (M): ", p1._Player__getTax("Italy"))

print ("\nQuiz - nothing major")

print ("\n3-D Point")
class Point:
    def __init__(self, label=None, x=0, y=0, z=0):
        self.label = label
        self.x = x
        self.y = y
        self.z = z

    # public method - square of sums
    def setPoint(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def getSqSum(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)

p1 = Point("mypoint", 3, 4, 5)
print (p1)
print ("Point: x:" + str(p1.x) + " y:" + str(p1.y) + " z:" + str(p1.z))
print (p1.getSqSum())
print (p1.setPoint(1, 3, 5))
print (p1.getSqSum())

print ("\nStudent")
class Student:
    # class attribute
    maxScore = 100
    
    def __init__(self, name=None, phy=0, chem=0, bio=0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def getTotalScore (self):
        return (self.phy + self.chem + self.bio)

    def getPercentScore (self):
        return ((self.getTotalScore()/(self.maxScore * 3)) * 100)

s1 = Student("Steve", 60, 70, 80)
print ("Total Score: " + str(s1.getTotalScore()))
print ("% Score: " + str(s1.getPercentScore()))

print ("\nCalculator")
class Calculator:
    def __init__(self, operand1=0, operand2=0):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

    def multiply(self):
        return self.operand1 * self.operand2

    def divide(self):
        return self.operand1 / self.operand2

c1 = Calculator(20, 5)
print (c1.add())
print (c1.subtract())
print (c1.multiply())
print (c1.divide())

    
