class Vehicle:
    company = 'Mercedes'
    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage
        print("init of vehicle ")

    def get_details(self):
        return f"this vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide a milage of {self.mileage}"

class Car(Vehicle):
    model = "UP420MC"
    def __init__(self, car_type, drive_type,n_wheels,n_seats, mileage):
        print("init of car ")
        self.car_type = car_type
        self.drive_type = drive_type
        # Vehicle.__init__(self,4,7,15)
        super().__init__(4,7,15)

    def display_info(self):
        print(f"car type : {self.car_type}, deive type : {self.drive_type}")
class ElectricCar(Car):
    model = "ElectricCar"
    def __init__(self, car_type, drive_type,n_wheels,n_seats, mileage,battery_capacity,range_distance):
        print("init of electric car ")
        self.battery_capacity = battery_capacity
        self.range_distance = range_distance
        super().__init__(car_type, drive_type,n_wheels, n_seats , mileage)

    def charge(self):
        print(f"charging the car to : {self.battery_capacity}")

elct_1 = ElectricCar("sadan","Manual",4,10,600,120,450)
print(elct_1.__dict__)
