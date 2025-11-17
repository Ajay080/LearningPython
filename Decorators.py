import time 


# 1 make a variable readable and writable using property decorator


# class Car:
#     totalCars = 0  # class variable to keep track of total cars

#     __carCount = 0  # private class variable

#     def __init__(self, make, model, year):
#         self.make= make
#         self.__model = model #made model private, now it cant be accessed directly from outside the class
#         self.year = year
#         Car.totalCars += 1
#         Car.__carCount += 1

#     def get_model(self):
#         return self.__model
    
#     @property  #property decorator to access private attribute, making it read-only
#     def model(self):
#         return self.__model 

#     @model.setter #setter to make the private attribute writable
#     def model(self, value):
#         self.__model = value    
    
#     @model.deleter #deleter to delete the private attribute
#     def model(self):
#         del self.__model

# toyota_car= Car("Toyota", "Camry", 2020)
# print(toyota_car.make)  # Accessible
# print(toyota_car.year)  # Accessible
# # print(toyota_car.__model)  # Not Accessible, will raise AttributeError    
# print("model using getter:", toyota_car.model)  # Accessing private attribute using getter, prints "Camry"
# print(toyota_car.get_model())  # Prints "Camry"
# toyota_car.model = "Corolla"  # Using setter to modify the private attribute
# print(toyota_car.model)  # Using getter to access the modified private attribute, prints


#1 end to make a variable readable and writable using property decorator


# 2 make a simple decorator function

# class GasolineCar:

#     # decoratoor function

#     def engine_decorator(func):
#         def wrapper():
#             print("Preparing to start the engine...   ", time.time())
#             func()
#             print("Engine started successfully!", time.time())
#         return wrapper

#     @engine_decorator
#     def start_engine():
#         print("Starting gasoline engine...")   


    
# GasolineCar.start_engine()

# 2 end make a simple decorator function

# 3 Decorator with parameters
# class GasolineCar:

#     # decoratoor function

#     def engine_decorator(func):
#         def wrapper(horsepower, engine_type):
#             print(f"Preparing to start the {engine_type} engine with {horsepower} HP...   ", time.time())
#             func(horsepower, engine_type)
#             print("Engine started successfully!", time.time())
#         return wrapper

#     @engine_decorator
#     def start_engine(horsepower, engine_type):
#         print(f"Starting {engine_type} engine with {horsepower} HP...")

# GasolineCar.start_engine(300, "V6")


# 3 end Decorator with parameters

# 4 Multiple decorators
# class GasolineCar:

#     # decoratoor function

#     def engine_decorator(func):
#         def wrapper(horsepower, engine_type):
#             print(f"Preparing to start the {engine_type} engine with {horsepower} HP...   ", time.time())
#             func(horsepower, engine_type)
#             print("Engine started successfully!", time.time())
#         return wrapper

#     def log_decorator(func):
#         def wrapper(horsepower, engine_type):
#             print(f"Logging: Engine of type {engine_type} with {horsepower} HP is about to start.")
#             func(horsepower, engine_type)
#             print("Logging: Engine has started successfully.")
#         return wrapper

#     @log_decorator
#     @engine_decorator
#     def start_engine(horsepower, engine_type):
#         print(f"Starting {engine_type} engine with {horsepower} HP...")

# GasolineCar.start_engine(300, "V6")


# 4 end Multiple decorators

# 5 Repeated Decorators

def repeat(num_times):
    def  decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")   

greet("Alice")