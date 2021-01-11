import math


class Car:
    def __init__(
        self, year, manufacturer, model, miles_per_gallon, fuel_tank, top_speed
    ):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.odometer_reading = 0
        self.fuel_tank = fuel_tank
        self.remaining_fuel = fuel_tank
        self.miles_per_gallon = miles_per_gallon
        self.max_distance = self.fuel_tank * self.miles_per_gallon
        self.top_speed = top_speed

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer.title()} {self.model.title()}"
        return long_name

    def get_odometer_reading(self):
        return self.odometer_reading

    def set_odometer(self, distance):
        self.odometer_reading += distance
        return self.odometer_reading

    def get_remaining_fuel(self):
        return self.remaining_fuel

    def refuel_fuel_tank(self):
        self.remaining_fuel = self.fuel_tank
        return {
            "fuel_remaing": self.get_remaining_fuel(),
            "message": f"{self.model.title()} refueled!",
        }

    def distance_traveled(self, distance):
        fuel_consumed = distance / self.miles_per_gallon
        refuels = math.floor(fuel_consumed / self.fuel_tank)
        delta_fuel = fuel_consumed % self.fuel_tank
        self.remaining_fuel = self.remaining_fuel - delta_fuel
        if self.remaining_fuel < 0:
            refuels += 1
            self.remaining_fuel = self.fuel_tank - abs(self.remaining_fuel)
        self.set_odometer(distance)
        time_driving_at_top_speed = distance / self.top_speed
        report = {
            "fuel_remaing": self.remaining_fuel,
            "refuels_for_trip": refuels,
            "odometer_reading": self.get_odometer_reading(),
            "distance_traveled_trip": distance,
            "time_driving_at_top_speed": time_driving_at_top_speed,
        }

        return report
