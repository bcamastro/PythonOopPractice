# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class vehivle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage





# OOP Exercise 2: Create a Vehicle class without any variables and methods

# class vehicle:
#     pass






# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# given:
# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#expected output: Vehicle Name: School Volvo Speed: 180 Mileage: 12

# class vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class bus(vehicle):
#     pass
# School_bus = Bus("School Volvo", 180, 12)







# OOP Exercise 4: Class Inheritance
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity}"
    
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
bus1 = Bus("bus1", 85, 32000)
print(bus1.seating_capacity())

#for this one I changed based off the answer board. I coded it a different way, not using the super() function, however after
#reviewing the answer sheet, I realized using super would make sense here since this code is implying more sibling classes may
# be added and need to use inheritance, so to avoid future errors, super() is the proper way.