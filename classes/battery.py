class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size
        self.remaining_battery = battery_size

    def describe_battery(self):
        print(f"{self.remaining_battery}/{self.battery_size} charge remaining")

    def update_battery(self, n):
        self.remaining_battery = n
        return self.remaining_battery
