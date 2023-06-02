class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт, мене звати {self.name} і мені {self.age} років.")

class Robot:
    def __init__(self, name):
        self.name = name

    def greet_person(self, person):
        print(f"Привіт, {person.name}! Я {self.name}. Радий познайомитись.")

person_1 = Person("Олег", 25)
person_2 = Person("Анна", 30)
robot = Robot("Робі")

person_1.introduce()
person_2.introduce()

robot.greet_person(person_1)
robot.greet_person(person_2)