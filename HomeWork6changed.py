from collections import UserDict
from datetime import datetime as dtdt

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
            
    def format_phone_number(add_phone):
        if phone.isdigit() and len(phone) == 10:
            return f"{phone[:3]}-{phone[3:6]}-{phone[6:]}"
        else:
            return "Invalid phone number format"

    def edit_phone(self, index, new_phone):
        try:
            self.phones[index] = Phone(new_phone)
        except IndexError:
            print("Invalid index")

    def delete_phone(self, index):
        try:
            del self.phones[index]
        except IndexError:
            print("Invalid index")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    
    def user_bd():
        while True:
                bday = input('Please typy your birthday(YYYY-MM-DD): ')

                if len(bday) == 8 and bday.isdigit():
                    try:
                        bday_formatted = dtdt.strptime(bday, '%Y%m%d')
                        return bday_formatted

                    except ValueError:
                        print("Invalid input. Please, use 'YYYY-MM-DD' format")
                    else:
                        print("Invalid input. Please, use 'YYYY-MM-DD' format")

class AddressBook(UserDict):
    def add_contact(self, record):
        self.data[record.name.value] = record

    def edit_contact(self, name, new_record):
        if name in self.data:
            self.data[name] = new_record
        else:
            print(f"Contact {name} not found")
    
    def find_contact(self, name, phones, birthday):
        if name in self.data:
             return  f"User Name: {self.name}, Phone Number: {self.phones}, Birthday: {self.birthday}"
        else:
            print(f"Contact {name} doesn`t exist")

    def delete_contact(self, name,phone):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact {name} can`t be deleted. This contact doesn`t exist")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return "An error occurred. Please check given information."

    return inner

@input_error
def add_contact(args, contacts, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, contacts):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.edit_contact(name, record)
    return "Contact successfully updated."

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))
            try:
                print(add_contact(args, contacts))
            except Exception as e:
                print(f"An error occurred: {e}")


        elif command == "change":
            print("Changing contact...")
            try:
                print(change_contact(args, contacts))
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == "phone":
            def show_phone(args, book):
                return [{contact.name.value: contact.phones} for contact in book.data.values()]

        elif command == "all":
            def show_contcts(args, book):
                return [contact.name.value]

        elif command == "add-birthday":
            def add_birthday(args, book):
                return  [[contact.name.value]+ {contact.birthday} for contact in book.data.values()]

        elif command == "show-birthday":
            def show_birthday(args, book):
                return f'[[contact.name.value]: {contact.birthday} for contact in book.data.values()]'
            
        elif command == "birthdays":
            def birthdays(args, book):
                return  f'{User:[contact.name.value], Birthday:{contact.birthday} for contact in book.data.values()}
        
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()