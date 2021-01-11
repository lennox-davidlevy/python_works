class Dog:
    def __init__(self, name, age, breed='unknown'):
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} has rolled over")

    def speak(self):
        print(f"{self.name} says: 'Bark!'")

    def what_breed(self):
        print(f"{self.name} is of the breed: {self.breed}")


    
satchmo = Dog('Satchmo', 10)

print(f"My dog's name is {satchmo.name}")
print(f"my dog is {satchmo.age} years old")
satchmo.roll_over()
satchmo.sit()
satchmo.speak()
satchmo.what_breed()
