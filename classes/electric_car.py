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

    def upgrade_battery(self, n):
        self.battery.upgrade_battery(n)
        self.fuel_tank = n
        return self.battery.battery_size

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
