from car import Car
from battery import Battery


class Electric_Car(Car):
    def __init__(
        self, year, manufacturer, model, miles_per_charge, battery_size, top_speed
    ):
        super().__init__(
            year, manufacturer, model, miles_per_charge, battery_size, top_speed
        )

        self.battery = Battery(battery_size, miles_per_charge)

    def distance_traveled(self, distance):
        travel_report = super().distance_traveled(distance)
        travel_report["battery_remaining"] = travel_report["fuel_remaing"]
        self.battery.update_battery(travel_report["battery_remaining"])
        del travel_report["fuel_remaing"]
        travel_report["recharges_for_trip"] = travel_report["refuels_for_trip"]
        del travel_report["refuels_for_trip"]
        return travel_report

    def recharge_battery(self):
        recharge_report = super().refuel_fuel_tank()
        recharge_report["battery_remaining"] = recharge_report["fuel_remaing"]
        self.battery.update_battery(recharge_report["battery_remaining"])
        del recharge_report["fuel_remaing"]
        recharge_report["message"] = f"{self.model.title()} has been recharged!"
        return recharge_report

    def get_current_range(self):
        current_range = self.battery.remaining_battery * self.battery.miles_per_charge
        print(f"Current range: {current_range}")
        return current_range

    def get_max_range(self):
        max_range = self.battery.battery_size * self.battery.miles_per_charge
        print(f"Max range: {max_range}")
        return max_range


my_tesla = Electric_Car("2019", "tesla", "model s", 4, 100, 155)
my_f150 = Car(2020, "ford", "f-150", 20, 23, 130)
my_prius = Car(2020, "toyota", "prius", 58, 11.3, 112)
print("\n")
# print(my_tesla.recharge_battery())  # print(my_tesla.get_descriptive_name())
# print("\n")
# print(my_tesla.distance_traveled(45))  # print(my_tesla.distance_traveled(300))
# print(my_tesla.distance_traveled(45))  # print(my_tesla.distance_traveled(300))
# print(my_tesla.distance_traveled(45))  # print(my_tesla.distance_traveled(300))
# print("-------------------------")
# print(my_f150.get_descriptive_name())
# print(my_f150.distance_traveled(10000))
# print("-------------------------")
# print(my_prius.get_descriptive_name())
# print(my_prius.distance_traveled(10000))
# print("-------------------------")
# print(my_tesla.get_descriptive_name())
# print(my_tesla.distance_traveled(10000))
# print("-------------------------")
# print(my_tesla.recharge_battery())
# print(my_f150.refuel_fuel_tank())
print(my_tesla.get_descriptive_name())
print(my_tesla.distance_traveled(200))
print(my_tesla.get_current_range())
print("-------------------------")
print(my_f150.get_descriptive_name())
print(my_f150.distance_traveled(200))
print(my_f150.get_current_range())
print("-------------------------")
print(my_prius.get_descriptive_name())
print(my_prius.distance_traveled(200))
print(my_prius.get_current_range())
print("-------------------------")
print(my_tesla.get_descriptive_name())
print(my_tesla.distance_traveled(200))
print(my_tesla.get_current_range())
print("-------------------------")
print(my_f150.get_descriptive_name())
print(my_f150.distance_traveled(200))
print(my_f150.get_current_range())
print("-------------------------")
print(my_prius.get_descriptive_name())
print(my_prius.distance_traveled(200))
print(my_prius.get_current_range())
