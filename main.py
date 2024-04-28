
from addressBook import AddressBook
from record import Record

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(book.add(args))

        elif command == "change":
            print(book.change(args))

        elif command == "phone":
            print(book.phone(args))

        elif command == "all":
            book.print_all()

        elif command == "add-birthday":
            print(book.add_birthday(args))

        elif command == "show-birthday":
            print(book.show_birthday(args))

        elif command == "birthdays":
            book.print_birthdays()

        else:
            print("Invalid command.")

def parse_input(inputString: str):
    strippedString = inputString.strip()
    if " " in strippedString:
        splitted = strippedString.split(" ")
        return splitted[0].lower(), *splitted[1:]
    return strippedString, 


main()
