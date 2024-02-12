def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."

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
        

