class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open = False
    def describe_restaurant(self):
        print(f"{self.name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        self.open = True
        print(f"{self.name.title()} is now open!")


gyro_world = Restaurant('gyro world', 'Greek Restaurant')
gyro_world.describe_restaurant()
gyro_world.open_restaurant()

