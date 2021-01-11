class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open = False
        self.number_servered = 0
    def describe_restaurant(self):
        print(f"{self.name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        self.open = True
        print(f"{self.name.title()} is now open!")

    def set_number_served(self,n):
        if n < 0:
            return
        self.number_servered += n
        
    def show_number_served(self):
        return self.number_servered



# gyro_world = Restaurant('gyro world', 'Greek Restaurant')
# gyro_world.describe_restaurant()
# gyro_world.open_restaurant()

