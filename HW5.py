1
cache = {}

def caching_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = caching_fibonacci(n - 1) + caching_fibonacci(n - 2)
        return cache[n]

fib = caching_fibonacci(10)
print(fib)
2
from typing import Callable, Dict
import re

with open('my_file.txt', 'w') as file_path:
    file_path.write('Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.')

def generator_numbers(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

def apply_discount(main_income: float, ex_income1: float, ex_income2: float) -> float:
    sum_profit = main_income + ex_income1 + ex_income2
    return sum_profit

total_dict: Dict[str, float] = {
    'main_income': 1000.01,
    'ex_income1': 27.45,
    'ex_income2': 324.00
}

total_income = apply_discount(**total_dict)
print(f"Загальний дохід: {total_income}")
4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            name, phone = args
        except ValueError:
            return "Give me name and phone number, please."
        except KeyError:
            return "No User information founded"
        except IndexError:
            return "Please, check your phone number or name. Possible issues:\nPerhaps this name is already taken!\nThe number consists of unacceptable symbols! "

        return inner   

@input_error   
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact successfuly updated."

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add username":
            print(add_contact(args, contacts))
        elif command == "change username":
            print(change_contact(args, contacts))
        elif command == "add user phone number":
            print(add_contact(args, contacts))
        elif command == "change my phone number":
            print(change_contact(args, contacts))
        elif args[0].isdigit():
            print("Phone number:", args[0])
        else:
            print("Invalid command.")

     
@input_error

    
if __name__ == "__main__":
    main()
