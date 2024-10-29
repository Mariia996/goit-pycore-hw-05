from constants import MENU, MESSAGES, ERROR_MESSAGES
from exceptions import InvalidCommand, NoContactFound, ContactAlreadyExists, input_error
from colorama import Fore


@input_error
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    capitalized_name = name.capitalize()
    if capitalized_name in contacts:
        raise ContactAlreadyExists()

    contacts[capitalized_name] = phone
    return MESSAGES["contact_added"]


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    capitalized_name = name.capitalize()
    if capitalized_name not in contacts:
        raise NoContactFound()

    contacts[capitalized_name] = phone
    return MESSAGES["contact_changed"]


@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0].capitalize()
    return f"{Fore.GREEN}{contacts[name]}"


@input_error
def show_all(contacts: dict) -> str:
    if not len(contacts):
        return MESSAGES["contacts_empty"]
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts = all_contacts + f"{Fore.GREEN} {name}: {phone}\n"

    return all_contacts


def main():
    """
    This is a bot for saving, changing and reviewing phone contacts.
    """
    contacts = {}
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = input(MESSAGES["enter_command"])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(MESSAGES["bye"])
                break

            match command:
                case "hello":
                    print(MESSAGES["help_question"])
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(show_phone(args, contacts))
                case "all":
                    print(show_all(contacts))
                case _:
                    raise InvalidCommand(ERROR_MESSAGES["invalid_command"])

        except InvalidCommand as e:
            print(e)
            continue


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
