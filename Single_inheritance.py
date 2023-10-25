class vehicle:
    def __init__(self,milage,cost,engine):
        self.milage=milage
        self.cost=cost
        self.engine=engine
    def show_vehicle_details(self):
        print("milage of vehicle is",self.milage)
        print("cost	 of vehicle is",self.cost)
        print("engine of vehicle is",self.engine)
v1=vehicle(300,500,"petrol")
v1.show_vehicle_details()
class car(vehicle):
    def show_vehicle_details(self):
        print("i am a automatic car")
c1=car(34,4500,"diesel")
c1.show_vehicle_details()
        
        