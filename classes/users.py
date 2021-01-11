class User:
    def __init__(self, first_name, last_name, age, location):
        self.fullname = f"{first_name.title()} {last_name.title()}"
        self.age = age
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        print(f"{self.fullname} is {self.age} years old from {self.location}")

    def greet_user(self):
        print(f"You say hello to {self.fullname}, {self.fullname} says 'Hi'")

    def increment_login_attempts(self):
        if self.login_attempts >= 10:
            self.login_attempts += 1;
            return 'LOCKED OUT TOO MANY LOGIN ATTEMPTS'
        self.login_attempts += 1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"login attempts reset, login count currently {self.login_attempts}")
