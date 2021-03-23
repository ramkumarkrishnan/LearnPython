# Object Relationships

print ("\nAggregation - Has-A relationship")
print ("Example - Country has many persons")

class Country:
    def __init__(self, name=None, population=0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country Name:", self.name)
        print("Country Population", self.population)

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person Name:", self.name)
        self.country.printDetails()


c = Country("India", 1500)
p = Person("Raj", c)
p.printDetails()

del p
c.printDetails()

print ("\nComposition - Part-Of relationship")
print ("Example - A Car is composed of many parts")

class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def Start(self):
        print("Engine started")

    def Stop(self):
        print("Engine stopped")

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car color:", self.color)

c = Car(1600, 4, 2, "Red")
c.printDetails()

print ("\nCars and Sedans")
print ("The Car parent only has a reference to Engine capacity attribute")
print ("and not the Engine object.  So you need to add a property that")
print ("refers to the Engine object, and then reuse its methods")
class Sedan(Car):
    def __init__(self, eng, tr, dr, color):
        super().__init__(eng, tr, dr, color)
        self.engine = Engine()

    def SedanStart(self):
        self.engine.Start()
        
    def SedanStop(self):
        self.engine.Stop()

s1 = Sedan(2000, 5, 4, "Metallic Blue")
s1.SedanStart()
s1.SedanStop()
s1.printDetails()

print ("\nSports Teams")
class Player:
    def __init__(self, Id=None, name=None, teamName=None):
        self.Id = Id
        self.name = name
        self.teamName = teamName

    def printPlayer(self):
        print("Player: " + str(self.Id) + " Name: " + str(self.name) +
              " TeamName: " + str(self.teamName))

class Team:
    def __init__(self, name=None, players=[]):
        self.name = name
        self.players = players

    def addPlayer(self, player):
        self.players.append(player)

    def getPlayerCount(self):
        return len(self.players)
        
    def printTeam(self):
        print("TeamName: " + str(self.name))
        print("Players: ", self.players)
        for p in self.players:
            p.printPlayer()


class School:
    def __init__(self, name=None, teams=[]):
        self.name = name
        self.teams = teams

    def addTeam(self, team):
        self.teams.append(team)
    
    def printSchool(self):
        print("School: ", self.name)
        print("Teams: ", self.teams)
        for t in self.teams:
            t.printTeam()

p1 = Player("01", "Salah", "Liverpool")
p2 = Player("02", "Mane", "Liverpool")
p3 = Player("03", "Henderson", "Liverpool")
p = [p1, p2, p3]
t1 = Team("Liverpool", p)
q1 = Player("10", "Aguero", "Man City")
q2 = Player("11", "De Bruyne", "Man City")
q3 = Player("12", "Mahrez", "Man City")
q = [q1, q2, q3]
t2 = Team ("Man City", q)
t = [t1, t2]
s = School("St Josephs", t)
s.printSchool()
print (t1.getPlayerCount())
print (t2.getPlayerCount())
p4 = Player("04", "Van Dijk", "Liverpool")
t1.addPlayer(p4)
print (t1.getPlayerCount())
s.printSchool()
