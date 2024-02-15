# 1
from pathlib import Path
workers = [
    ('Alex Korp', 3000),
    ('Nikita Borisenko', 2000),
    ('Sitarama Raju', 1000)
]

with open('w_salary.txt', 'w') as sal_count:
    for _, salary in workers:
        sal_count.write(f"{salary}\n")
path = Path('C:/Users/111/Desktop/Game/w_salary.txt')

def total_salary(file_path):
    with open(file_path, 'r') as sal_count:
        lines = sal_count.readlines()

total, average = total_salary(path)

try:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError:
    print(f'The file {file_path} doesn`t exist')



# 2
from pathlib import Path

cats = [
    ('60b90c1c13067a15887e1ae1', 'Tayson', 3),
    ('60b90c2413067a15887e1ae2', 'Vika', 1),
    ('60b90c2e13067a15887e1ae3', 'Barsik', 2),
    ('60b90c3b13067a15887e1ae4', 'Simon', 12),
    ('60b90c4613067a15887e1ae5', 'Tessi', 5),
]

directory_path = Path('C:/Users/111/Desktop/GAME')

with open(directory_path / 'c_list.txt', 'w') as cat_info:
    for cat in cats:
        id, name, age = cat
        cat_info.write(f"ID: {id}\nName: {name}\nAge: {age}\n")

def get_cats_info(file_path):
    with open(file_path, 'r') as cat_info:
        return cat_info.readlines()
cats_info = []
for i in range(0, len(lines), 3):
        id_line, name_line, age_line = lines[i:i + 3]
        
        cat_id = id_line.strip().split(': ')[1]
        cat_name = name_line.strip().split(': ')[1]
        cat_age = age_line.strip().split(': ')[1]

        cat_dict = {"id": cat_id, "name": cat_name, "age": cat_age}
        cats_info.append(cat_dict)

return cats_info

cats_info = get_cats_info(directory_path / 'c_list.txt')
print(cats_info)

# 4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact successfuly updated."

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

if __name__ == "__main__":
    main()
