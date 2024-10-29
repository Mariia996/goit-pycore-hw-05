from constants import ERROR_MESSAGES


class InvalidCommand(Exception):
    pass


class NoContactFound(Exception):
    pass


class ContactAlreadyExists(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return ERROR_MESSAGES["phone_and_number_missing"]
        except IndexError:
            return ERROR_MESSAGES["phone_missing"]
        except KeyError:
            return ERROR_MESSAGES["no_contact"]
        except ContactAlreadyExists:
            return ERROR_MESSAGES["contact_already_exists"]
        except NoContactFound:
            return ERROR_MESSAGES["no_contact"]

    return inner
