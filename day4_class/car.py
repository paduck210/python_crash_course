class Car:

    def __init__(self, make, model, year, country="German"):
        self.make = make
        self.model = model
        self.year = year
        self.country = country
        self.meter = 0

    def get_descriptvie_name(self):
        long_name = f"{self.year} {self.make} {self.model} - made in {self.country}"
        return(long_name.title())

    def read_meter(self):
        return(f"This car has {self.meter} on it")

    def update_meter(self, number):
        self.meter = number

    def increase_meter(self, number):
        self.meter += number


class Battery:

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def battery_size_check(self):
        return(f"{self.battery_size * 100} remain")

    def get_range(self):
        if self.battery_size >= 75:
            return("Not bad, 75")
        else:
            return(f"Too bad, you will be dead - {self.battery_size}")


class ElectricCar(Car):

    def __init__(self , make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def read_meter(self):
        return("We don't have meter, try to call battery_size instead of it")
