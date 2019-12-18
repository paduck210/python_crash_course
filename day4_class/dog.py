class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_name(self):
        return(f"{self.name} is now enjoying")

    def expected_age(self):
        return(self.age + 10)


my_dog = Dog('Willy', 6)
print(my_dog.name)
print(my_dog.call_name())
print(my_dog.expected_age())