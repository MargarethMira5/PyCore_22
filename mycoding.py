# import random
# class UAcademy:
#     fam = "Hargreeves` Family"

#     def __init__(self, name = str, age = int) -> None:
#         self.name = name
#         self.age = age
        
    
#     def five_sup_power(self):
#         sp_list = ['telekinesis', 'flight', 'teleportation', 'invisibility', 'super strength']
#         random.shuffle(sp_list)
#         print(self.name)
#         print(self.age)
#         print(sp_list[:5])
        

#     def lutor_sup_power(self):
#         lut_sp = 'hit,hit,hit,hit,hit'
#         res_sp = lut_sp.upper()
#         print(self.name)
#         print(self.age)
#         print(res_sp)

# # Create instances of UAcademy
# five = UAcademy('Five', 13)
# lutor = UAcademy('Lutor', 25)

# # Call the methods for each instance
# print(five.fam)
# five.five_sup_power()
# print(lutor.fam)
# lutor.lutor_sup_power()

# class Pokemon:
#     def __init__(self, name, type, health):
#         self.name = name
#         self.type = type
#         self.health = health

#     def attack(self, other_pokemon):
#         print(f"{self.name} attacks {other_pokemon.name}!")

#     def dodge(self):
#         print(f"{self.name} dodged the attack!")

#     def evolve(self, new_form):
#         print(f"{self.name} is evolving into {new_form}!")
#         self.name = new_form

# # Створення об'єкта Pikachu
# pikachu = Pokemon("Pikachu", "Electric", 100)

# # Використання методів
# pikachu.attack(Pokemon("Charmander", "Fire", 100))
# pikachu.dodge()
# pikachu.evolve("Raichu")

# from typing import Callable
# import re
# import math

# with open('my_file.txt', 'w') as file_path:
#     file_path.write('Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.')

# def generator_numbers(text: str):
#     numbers = re.findall(r'\d+\.\d+|\d+', text)
#     for numb in numbers:
#         yield float(numb)

# def sum_profit(text: str, func: Callable):
#     numbers_generator = func(text)
#     return sum(numbers_generator)

# with open('my_file.txt', 'r') as file:
#     file_content = file.read()

# total_income = sum_profit(file_content, generator_numbers)
# print(f"Загальний дохід: {total_income}")

# from typing import Callable, Union

# def apply_operation(x: Union[int, float], y: Union[int, float], operation: Callable[[Union[int, float], Union[int, float]], Union[int, float]]) -> Union[int, float]:
#     return operation(x, y)

# def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
#     return x + y

# def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
#     return x * y

# result_add = apply_operation(3, 4, add)
# result_multiply = apply_operation(3, 4.5, multiply)

# print(result_add)       # Output: 7
# print(result_multiply)  # Output: 13.5

# from typing import Callable

# def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
#     return operation(x, y)

# def add(x: int, y: int) -> int:
#     return x + y

# def multiply(x: int, y: int) -> int:
#     return x * y

# result_add = apply_operation(3, 4, add)
# result_multiply = apply_operation(3, 4, multiply)

# print(result_add)       # Output: 7
# print(result_multiply)  # Output: 12

# from typing import Callable

# def concatenate_strings(x: str, y: str, operation: Callable[[str, str], str]) -> str:
#     return operation(x, y)

# def string_concatenation(x: str, y: str) -> str:
#     return x + y

# result_concatenate = concatenate_strings("Hello", " World!", string_concatenation)
# print(result_concatenate)  # Output: Hello World!



# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

#     @classmethod
#     def create_student(cls, fname, lname):
#         # This is a class method that creates a Student instance
#         return cls(fname, lname)

# fn = input('First Name: ', self.firstname)
# ln = input('Last Name: ', self.lastname)

# x = Person.create_student(fn, ln)
# x.printname()

# class Animal:
#     def __init__(self, nickname: str, age: int):
#         self.nickname = nickname
#         self.age = age

#     def make_sound(self):
#         pass

# class Cat(Animal):
#     def info(self):
#         print('Nickname: ',self.nickname,'Age: ',self.age)
#     def make_sound(self) -> str:
#         return "Meow"

# class Dog(Animal):
#     def info(self):
#         print('Nickname: ',self.nickname,'Age: ',self.age)
#     def make_sound(self) -> str:
#         return "Woof"

# class Cow(Animal):  
#     def info(self):
#         print('Nickname: ',self.nickname,'Age: ',self.age)
#     def make_sound(self):
#         return "Moo"

# my_cat = Cat("Simon", 4)
# my_dog = Dog("Rex", 5)
# my_cow = Cow("Bessie", 3)

# print(my_cat.info())
# print(my_cat.make_sound())  

# print(my_dog.info())
# print(my_dog.make_sound())  
 
# print(my_cow.info()) 
# print(my_cow.make_sound()) 

# from collections import UserDict

# contacts = [
#     {
#         "name": "Luthor Hargreeves",
#         "email": "NumbOne@gmail.com",
#         "phone": "(000) 000-0000",
#         "favorite": False,
#     },
#     {
#         "name": "Ben Hargreeves",
#         "email": "Number6octop@gmail.com",
#         "phone": "(000) 000-0000",
#         "favorite": False,
#     },
#     {
#         "name": "Five Hargreeves",
#         "email": "5HUmAc@gmail.com",
#         "phone": "(000) 000-0000",
#         "favorite": True,
#     }
# ]

# class H_fam(UserDict):
#     def phone_info(self):
#         return f"{self.get('name')}: {self.get('phone')}"

#     def email_info(self):
#         return f"{self.get('name')}: {self.get('email')}"

# if __name__ == "__main__":
#     members = [H_fam(el) for el in contacts]

#     print("---------------------------")

#     for Child in members:
#         print(Child.phone_info())

#     print("---------------------------")

#     for Child in members:
#         print(Child.email_info())

# print(dir(UserList))
# current_list = [[10,6,9],[0, 14, 16, 80],[8, 12, 30, 44]]
# sorted_list = lambda x: (sorted(i) for i in x)
# second_largest = lambda x, func: [y[len(y)-4] for y in func(x)]
# result = second_largest(current_list, sorted_list)
# print(result)

# Store = [
#     {"National": {"apples": 5, "cherries": 10, "strawberries": 10}},
#     {"Exotic": {"banana": 10, "mango": 20}}
# ]

# print(Store[:-1])

def calculate_spaces(words):
    answer = 0
    for i in words:
        if i == ' ':
            answer += 1
    return answer

words = 'a b c'
print(calculate_spaces(words))  
