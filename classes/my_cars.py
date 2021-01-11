from car import Car
from electric_car import Electric_Car


my_subaru = Car(2020, "subaru", "forrester", 30, 20, 130)
my_tesla = Electric_Car(2020, "tesla", "model s", 4, 100, 155)
print(my_subaru.get_descriptive_name())
print(my_tesla.get_descriptive_name())
