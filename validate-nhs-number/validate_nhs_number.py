"""
The NHS App team have had a new requirement to validate all new NHS numbers through the PDS API. 
We need to check that the NHS number is valid.

- does not start with 0
- contains no alphabetic characters
- length is exactly 10 characters
- contains no special characters, i.e. !@#$%^&*()-+_
- contains no blank spaces

STEP 1 - Starting from the left, multiply each of the first nine digits by (10 - digit position). For example contents of digit position 1 would be multiplied by 10, contents of digit position 2 by 9, contents of digit position 3 by 8, etc.
STEP 2 - Add the results of the nine multiplications together.
STEP 3 - Divide the total by 11 and obtain the remainder.
STEP 4 - Subtract the remainder from 11 to get the calculated check digit. If the calculated check digit is 11, substitute a value of 0. If the calculated check digit is 10, then it is an invalid NHS number.
STEP 5 - Validate your calculated check digit against the final digit in the NHS number (checksum)
"""


SPECIAL_CHARACTERS = "!@#$%^&*()-+_"


def does_not_start_with_0(nhs_number: str):
    return nhs_number[0] != "0"


def no_alphabetic_characters(nhs_number: str):
    return nhs_number.isnumeric()


def is_10_chars(nhs_number: str):
    return len(nhs_number) == 10


def no_special_characters(nhs_number: str):
    for number in nhs_number:
        if number in SPECIAL_CHARACTERS:
            return False
    return True


def no_blank_spaces(nhs_number: str):
    return " " not in nhs_number


def is_nhs_number_valid(nhs_number: str):
    return all(
        [
            does_not_start_with_0(nhs_number),
            no_alphabetic_characters(nhs_number),
            is_10_chars(nhs_number),
            no_special_characters(nhs_number),
            no_blank_spaces(nhs_number),
        ]
    )
