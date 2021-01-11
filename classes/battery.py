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

    def upgrade_battery(self, n):
        if n > self.battery_size:
            print(f"Battery size updgraded from {self.battery_size}kWh to {n}kWh")
            self.battery_size = n
            return
        else:
            print(f"current battery has a larger capacity")
            return
