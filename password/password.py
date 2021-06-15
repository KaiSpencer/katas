"""
Function that validates password
Check has at least 1 uppercase
Check has at least 1 lowercase
Check has at least 1 number
Check has at least 1 symbol: *&%$£@%
"""

"""
Single function to validate password
Functions for each criteria
return if all criteria met
"""


def validate_password(password):
    return all(
        [
            validate_uppercase(password),
            validate_lowercase(password),
            validate_number(password),
            validate_symbol(password),
            validate_length(password),
        ],
    )


def validate_uppercase(password: str):
    for char in password:
        if char.isupper():
            return True
    return False


def validate_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def validate_number(password: str):
    # for char in password:
    #     if char.isnumeric():
    #         return True
    # return False

    return any([char.isnumeric() for char in password])


def validate_symbol(password):
    symbols = "*&%$£@%"
    # for symbol in symbols:
    #     if symbol in password:
    #         return True
    # return False

    return any([symbol in password for symbol in symbols])


def validate_length(password):
    return len(password) > 10
