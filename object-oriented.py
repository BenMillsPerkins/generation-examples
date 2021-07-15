# from typing import List, Dict

# def add_numbers(a: int, b: int) -> int: # This function return an int
#     return a + b

# new_number = add_numbers(5,7)

# def add_strings(a: str, b: str):
#     return a.


# print(new_number + 5)

# def print_cars(cars: List[Dict[str, str]]):
#     for car in cars:
#         print(f"Brand: {car['brand']}, Colour: {car['colour']}")

# cars = [{"brand": "BMW", "colour": "Blue"},
#         {"brand": "Volvo", "colour": "Red"}]

# print_cars(cars)

# def add_numbers(a: int, b) -> int: # This function return an int
#     return a + b

# jane = ['Jane Doe', 20,  175,   150]

# def increase_age(person):
#     person[1] = person[1] + 1
#     return person

# jane = increase_age(jane)
# print(jane)

# class Person:
#     def __init__(self, name, age):
#         print(name, age)
#         self.name = name
#         self.age = age
#         print("Created new person")

#     def increment_age(self):
#         self.age = self.age + 1

# jane = Person("Jane Doe", 20)

# def greet_person(person: Person):
#     print(f"Hello {person.name}")

# greet_person(jane)

# class Person:
#     def __init__(self, name, age):
#         print(name, age)
#         self.name = name
#         self.age = age
#         print("Created new person")

# jane = Person("Jane", 25)
# john = Person("John", 20)

# def greet_person(person: Person):
#     print(f"Hello {person.name}")

# # greet_person(john)
# # greet_person(jane)

# people = [jane, john]

# for person in people:
#     print(person.age)

# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour

#     def set_speed_500(self):
#         self.max_speed = 500

    # def change_speed(self, new_speed):
#         self.change_colour("Green")
#         self.max_speed = new_speed

#     def change_colour(self, new_colour):
#         self.colour = new_colour

# mustang = Vehicle(150, "Blue")
# print(mustang.colour)

# # print(mustang.max_speed)
# mustang.change_speed(200)
# # print(mustang.max_speed)


# print(mustang.colour)
# mustang.change_colour("Red")
# print(mustang.colour)


# class Person:
#     def __init__(self, name, email):
#         self.name = name.upper()
#         self.email = email

#     def email_person(self):
#         print(f"I have emailed {self.name} at {self.email}")

# class Teacher(Person):
#     def __init__(self, name, email, subject):
#         super().__init__(name, email)
#         self.subject = subject

#     def email_person(self):
#         print(f"I have emailed the teacher {self.name} who teaches {self.subject} at {self.email}")

#     def print_name(self):
#         print(f"The teacher's name is {self.name}")


# sam = Person("Sam", "sam@gmail.com")
# ben = Teacher("Ben", "ben@gmail.com", "Maths")
# ben.email_person()
# # ben.print_name()
# # sam.print_name()
# sam.email_person()

# print(dir(ben))

# class SuperString(str):
#     def __init__(self, val):
#         super().__init__()
#         self.val = val

#     def is_valid_int(self):
#         try:
#             int(self.val)
#             return True
#         except:
#             return False

# example = "This is a string"
# superExample = SuperString("67")
# print(example)
# print(superExample)
# print(superExample.is_valid_int())

class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour

    def change_speed(self, new_speed):
        self.max_speed = new_speed

    def change_colour(self, new_colour):
        self.colour = new_colour

    def __repr__(self):
        return repr(f"Max speed: {self.max_speed}, Colour: {self.colour}")


class Bus(Vehicle):
    def __init__(self, max_speed, colour, seating_capacity):
        super().__init__(max_speed, colour)
        self.seating_capacity = seating_capacity

    def calc_ticket_price(self):
        ticket_price = self.seating_capacity*0.055
        return ticket_price

    def __repr__(self):
        return repr(f"Max speed: {self.max_speed}, Colour: {self.colour}, Seating Capacity: {self.seating_capacity}")

    

big_red_bus = Bus(80, "Red", 132)
# print(big_red_bus.max_speed)
# print(big_red_bus.colour)


# print(type(big_red_bus))
# print(isinstance(big_red_bus, Vehicle))
# print(big_red_bus.calc_ticket_price())
print(repr(big_red_bus))

mustang = Vehicle(150, "Blue")
print(repr(mustang))
