class Car:
    totalCars = 0  # class variable to keep track of total cars

    __carCount = 0  # private class variable
    def __init__(self, make, model, year):
        self.make= make
        self.__model = model #made model private, now it cant be accessed directly from outside the class
        self.year = year
        Car.totalCars += 1
        Car.__carCount += 1
    def get_model(self):
        return self.__model

toyota_car= Car("Toyota", "Camry", 2020)
print(toyota_car.make)  # Accessible
print(toyota_car.year)  # Accessible
# print(toyota_car.__model)  # Not Accessible, will raise AttributeError    
toyota_car.__model = "Corolla"  # This creates a new attribute, does not modify the private one
print(toyota_car.get_model())  # Still prints "Camry"


# how to access this new attribute, it created a new attribute in the instance
print(toyota_car.__model)  # Prints "Corolla"


# we can access the private attribute using name mangling
print(Car.totalCars)  # Prints "Camry"
Car.totalCars += 1

print(Car.totalCars)  # Prints "2"
# print(Car.__carCount)  # Not Accessible, will raise AttributeError
# Accessing private class variable using name mangling
print(Car._Car__carCount)  # Prints "1"

class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower
        self.engine_type = engine_type

class BS400Engine(Engine): #single inheritance
    def __init__(self):
        super().__init__(horsepower=400, engine_type="V8")

class ElectricCar(Car, Engine): #multiple inheritance
    def __init__(self, make, model, year, battery_size):
        Car.__init__(self, make, model, year)
        Engine.__init__(self, horsepower=0, engine_type="electric")
        self.battery_size = battery_size

    # @property #property decorator to access private attribute, making it read-only
    def model(self):
        return self._Car__model
    
    def model1(self):
        return self.__model

    def get_battery_info(self):
        return f"{self.make} {self.get_model()} has a {self.battery_size}-kWh battery."

class GasolineCar(Car, Engine):
    def __init__(self, make, model, year, fuel_tank_size):
        super().__init__(make, model, year)
        self.fuel_tank_size = fuel_tank_size

    def get_fuel_info(self):
        return f"{self.make} {self.get_model()} has a {self.fuel_tank_size}-liter fuel tank."



tesla= ElectricCar("Tesla", "Model S", 2022, 100)
print(isinstance(tesla, ElectricCar))  # True
print(isinstance(tesla, Car))          # True
print(isinstance(tesla, Engine))       # True
print(tesla.get_battery_info())        # Tesla Model S has a 100-k

tesla.__model = "Model X"  # This creates a new attribute, does not modify the private
print(tesla.get_model())  # Still prints "Model S"Wh battery.

# tesla.model1= "Model X"  # This creates a new attribute, does not modify the private one
# print(tesla.model())  # Still prints "Model S"
print(tesla.model())  # Accessing the private attribute using property decorator, prints "Model S"



#Static Method
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
    def subtract(self, a, b):
        return a - b
    
    def sub(a, b):  # Static method without decorator
        return a - b

mat= MathOperations()

print(MathOperations.add(5, 3))        # 8
print(MathOperations.multiply(5, 3))   # 15
# print(MathOperations.subtract(5, 3))   # Error: subtract() missing 1 required positional argument: 'b'
print(mat.subtract(5, 3))   # 2 # Calling without instance, works fine
print(MathOperations.sub(5, 3))   # 2 # Calling without instance, works fine