def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print("Adding contact...")
            print(add_contact(args, contacts))
        elif command.startswith("change"):
            print("Changing contact...")
            print(change_contact(args, contacts))
        elif args and args[0].isdigit():
            print("Phone number:", args[0])
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()