from car import *

def run(car, number):
    car.battery.battery_size = number
    print(car.get_descriptvie_name())
    print(car.battery.battery_size_check())
    print(car.battery.get_range())


my_tesla = ElectricCar('tesla', 'model S', 2019)
run(my_tesla, 10)
