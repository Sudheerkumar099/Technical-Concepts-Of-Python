class Vehicle:
    def start(self):
        print("Vehicle Started")
    
        
class car(Vehicle):
   
    def start(self):
        print("Car is starting")

class Boat(Vehicle):
    
    def start(self):
        print("Boat is starting")

car = car()
Boat = Boat()
Vehicle = Vehicle()
for x in [car,Boat,Vehicle]:
    x.start()