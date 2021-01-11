class Battery:
    def __init__(self, battery_size, miles_per_charge):
        self.battery_size = battery_size
        self.remaining_battery = battery_size
        self.miles_per_charge = miles_per_charge

    def describe_battery(self):
        print(
            f"{self.remaining_battery}/{self.battery_size} charge remaining at {self.miles_per_charge}miles per kWh"
        )
        return {
            "remaining_battery": self.remaining_battery,
            "battery_size": self.battery_size,
            "miles_per_charge": self.miles_per_charge,
        }

    def update_battery(self, n):
        self.remaining_battery = n
        return self.remaining_battery
