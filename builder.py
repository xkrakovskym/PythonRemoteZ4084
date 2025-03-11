class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return(
       f"Car with {self.seats}, engine type {self.engine}, "
       f"trip computer: {'yes' if self.trip_computer else 'no'}, "
       f"GPS: {'yes' if self.gps else 'no'}"
        )


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_seats(self, number):
        self.car.seats = number
        return self

    def add_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def add_trip_computer(self):
        self.car.trip_computer = True
        return self

    def add_gps(self):
        self.car.gps = True
        return self

    def build(self):
        if self.car.seats in None:
            print("unbuildable car")
        return self.car


builder = CarBuilder()
sport_car = builder.add_engine("V8").add_trip_computer().build()

print(sport_car)