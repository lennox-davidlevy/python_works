from car import Car

my_car = Car(2006, 'honda', 'accord')
best_car = Car(1989, 'Lamborgini', 'contach')
worst_car = Car(2000, 'PT', 'Cruiser')

print(my_car.get_odometer_reading())
my_car.distance_traveled(50)
print(my_car.get_odometer_reading())
my_car.odometer_reading += 100
print(my_car.get_odometer_reading())

