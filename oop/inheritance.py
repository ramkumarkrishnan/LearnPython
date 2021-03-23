# Python OOP - Inheritance
class Vehicle:
    def __init__(self, make=None, color="White", model=None):
        self.make = make
        self.color = color
        self.model = model

    def printVehicle(self):
        print ("Vehicle:Make: " + str(self.make) + " Color: " +
               str(self.color) + " Model: " + str(self.model))

print ("\nVehicle")
v1 = Vehicle()
print ("Vehicle:printVehicle:")
v1.printVehicle()

class Car (Vehicle):
    def __init__(self,make =None, color=None, model=None,
                 vin=None, seats=0):
        #Vehicle.__init__ (self, make, color, model)
        # Alternatively, if you want to intervene in the constructor ...
        color = "Green"
        super().__init__(make, color, model)
        self.vin = vin
        self.seats = seats
        
    def printVehicle(self):
        super().printVehicle()
        
    def printCar(self):
        self.printVehicle()
        print ("Car: Vin: " + str(self.vin) + " Seats: " + str(self.seats))

print ("\nCar-Tesla")
#c1 = Car()
c1 = Car("Tesla", "Red", "Model 3", "ABC1234567890", 5)
print ("Tesla:printVehicle:")
c1.printVehicle()
print ("Tesla:printCar:")
c1.printCar()

print ("\nCar-Lucid")
c1 = Car("Lucid", "Metal Blue", "Air", "CBA0987654321", 7)
print ("Lucid:printVehicle:")
c1.printVehicle()
print ("Lucid:printCar:")
c1.printCar()

print ("\nTypes of Inheritance")
print ("\nSingle Inheritance - example above")
print ("\nMulti-level Inheritance")

class Hybrid (Car):
    def __init__(self, make=None, color=None, model=None, vin=None,
                 seats=0, drives=0, mpgeRating=0):
        # mpgeRating - N kWh/100m
        super().__init__(make, color, model, vin, seats)
        self.drives = drives
        self.mpgeRating = mpgeRating

    def printVehicle(self):
        super().printVehicle()

    def printCar(self):
        super().printCar()

    def printHybrid(self):
        self.printCar()
        print ("Hybrid: Drives: " + str(self.drives) +
               " mpgeRating: ", str(self.mpgeRating))

print ("\nCar-Prius")
h1 = Hybrid ("Prius", "Neon Green", "Prime", "BAC5432109876", 5, 2, 25)
print ("Lucid:printVehicle:")
h1.printVehicle()
print ("Lucid:printCar:")
h1.printCar()
print ("Prius:printHybrid:")
h1.printHybrid()

print ("\nHierarchical Inheritance")

class Truck (Vehicle):
    def __init__(self,make=None, color=None, model=None, vin=None,
                 towingCap=0, horsePower=0):
        #Vehicle.__init__ (self, make, color, model)
        # Alternatively, if you want to intervene in the constructor ...
        super().__init__(make, color, model)
        self.vin = vin
        self.towingCap = towingCap
        self.horsePower = horsePower
        
    def printVehicle(self):
        super().printVehicle()
        
    def printTruck(self):
        self.printVehicle()
        print ("Truck: Vin: " + str(self.vin) + " towingCap: " +
               str(self.towingCap) + " horsePower: " + str(self.horsePower))

print ("\nTruck-F-150")
t1 = Truck("Ford", "Red", "F-150", "ABC1234567890", 5000, 250)
print ("Ford:printVehicle:")
t1.printVehicle()
print ("Ford:printTruck:")
t1.printTruck()

print ("\nMultiple Inheritance")

class ICEngine():  
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class EVEngine():  
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from ICEngine and EVEngine
class HybridEngine(ICEngine, EVEngine):
    def printEngine (self):
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)

e1 = HybridEngine()
e1.setChargeCapacity("250 W")
e1.setTankCapacity("20 Litres")
e1.printEngine()

print ("\nBank Account Example")
class BankAccount:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def Deposit(self, deposit):
        self.__balance += deposit

    def Withdraw(self, withdrawal):
        self.__balance -= withdrawal

    def printAccount(self):
        print ("Account Holder: " + str(self.title) +
               " Balance: " + str(self.__balance))

class SavingsAccount(BankAccount):
    def __init__(self, title=None, balance=0, apr=0):
        super().__init__(title, balance)
        self.apr = apr

    def printSavingsAccount(self):
        super().printAccount();
        print ("APR: ", self.apr)

b1 = BankAccount("Steve", 5000)
print ("Account: " + str(b1.title) + " Balance: " + str(b1.getBalance()))

s1 = SavingsAccount("Martin", 4000, 0.01)
s1.Deposit(6000)
print ("Account: " + str(s1.title) + " Balance: " + str(s1.getBalance()) +
       " APR: " + str(s1.apr))
s1.Withdraw(2000)
print ("Account: " + str(s1.title) + " Balance: " + str(s1.getBalance()) +
       " APR: " + str(s1.apr) +
       " Interest: " + str(s1.getBalance() * s1.apr))
