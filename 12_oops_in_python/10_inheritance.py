class Vehicle:
    company = 'Mercedes'
    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"this vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide a milage of {self.mileage}"

# v1 = Vehicle(4,7,30)
# print(v1.get_details()) #this vehicle has 4 wheels and 7 seats and provide a milage of 30

class Car(Vehicle):
    model = "UP420MC"
    def __init__(self, car_type, drive_type,n_wheels, mileage,seats):
        print("init of car ")
        self.car_type = car_type
        self.drive_type = drive_type
        # Vehicle.__init__(self,4,7,15)
        super().__init__(4,7,15,40)

# the car class inherits the vehicle class
#car class is also called derived / child class
#vehicle class is called parent / base class
# c1 = Car(3, 8,9)

c2 = Car("SUV", "Automatic",4,7,15)
# print(c1.mileage)
# print(c1.n_seats)
print(c2.company)
print(c2.model)
print(c2.mileage)
print(c2.get_details())
print(c2.__dict__)


