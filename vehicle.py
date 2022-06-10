from time import time

class Vehicle:
    color="white"
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def congratulation(self):
        return f"congratulation on getting your first {self.color} {self.name} that drives with the max_speed of {self.max_speed}km/hr and covers adistance of {self.mileage} km"
    
    def cap(self,capacity):
        return f"The {self.name} that has the capacity of {capacity} seats"
    