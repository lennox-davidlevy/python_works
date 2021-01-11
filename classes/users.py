class User:
    def __init__(self, first_name, last_name, age, location):
        self.fullname = f"{first_name.title()} {last_name.title()}"
        self.age = age
        self.location = location
    def describe_user(self):
        print(f"{self.fullname} is {self.age} years old from {self.location}")

    def greet_user(self):
        print(f"You say hello to {self.fullname}, {self.fullname} says 'Hi'")

