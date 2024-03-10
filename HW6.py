from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
def __init__(self, name):
        self.name = Name(name)
        self.phones = []

def add_phone(self, phone):
        self.phones.append(Phone(phone))

def edit_phone(self, index, new_phone):
        if 0 <= index < len(self.phones):
            self.phones[index] = Phone(new_phone)
        else:
            print("Invalid index")

def delete_phone(self, index):
        if 0 <= index < len(self.phones):
            del self.phones[index]
        else:
            print("Invalid index")

def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_contact(self, record):
        self.data[record.name.value] = record


def edit_contact(self, name, new_record):
        if name in self.data:
            self.data[name] = new_record
        else:
            print(f"Contact {name} not found")

        def delete_contact(self, name):
            if name in self.data:
                del self.data[name]
            else:
                print(f"Contact {name} not found")

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



if __name__ == '__main__':
    print(main)

     