class Vehicle:
    company = 'Mercedes'
    def __init__(self, n_wheels, n_seats,milage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = milage

    def get_detaile(self):
        return f"this vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide a milage of {self.mileage}"

v1 = Vehicle(4,7,30)
print(v1.get_detaile()) #this vehicle has 4 wheels and 7 seats and provide a milage of 30

class Car(Vehicle):
    def __init__(self, car_type, drive_type):
        print("init of car ")
        self.car_type = car_type
        self.drive_type = drive_type

# the car class inherits the vehicle class
#car class is also called derived / child class
#vehicle class is called parent / base class
c1 = Car(3, 8, 60 )
c2 = Car("SUV", "Automatic")
# print(c1.mileage)
# print(c1.n_seats)
# print(c1.company)
print(c1.get_detaile())
help(c1)

