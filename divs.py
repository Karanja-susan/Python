class car:
    def __init__(self,model,year):
        self.model=model
        self.year=year

    def display(self):
     print("self.model,self.year")
     print(f"My dream car is {"self.model"} and my dream car is {"self.model"} manufactured in {"self.year"}")
c1 = car("Toyota",2016)
c1.display()

class Employee:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID

    def display(self):
        print("ID:%\nName:%\n: % (self.ID,self.name)")

empl1 = Employee("JOHNSON",101)
empl2 = Employee("JEYDWEL",102)

empl1.display()
empl2.display()

class gari:
    def __init__(self,make,model,year):
        self.make = make
        self.model =model
        self.year =year
        self.odemeter_reading =0
    def describe_gari(self):
        return f"{self.model} {self.year} {self.make}"
    def read_odemeter(self):
        return f"This car has {self.odemeter_reading} miles on it"

    def update_odemeter(self,milage):
        if milage >=self.odemeter_reading:
            self.odemeter_reading =milage
        else:
            print("You cant roll back an odometer")
    def increment_odemeter(self,miles):
        self.odemeter_reading +=miles
my_car=gari("Toyota","Vits",2024)
print(my_car.describe_gari())
print(my_car.read_odemeter())
my_car.update_odemeter(100)
print(my_car.read_odemeter())
# print(my_car.update_odemeter(100))
print(my_car.odemeter_reading)
my_car.increment_odemeter(50)
print(my_car.read_odemeter())