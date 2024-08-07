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

class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(vehicle):
    pass
School_bus = Bus("School Volvo", 180, 12)
