class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Cat named {self.name}"


# Create a new Dog object
my_dog = Dog("Buddy", 3)

print(my_dog.name)  # Buddy
print(my_dog.age)  # 3

print(Cat("Rudy"))  # Cat named Rudy

print(__name__)
