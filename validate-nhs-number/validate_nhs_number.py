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

from typing import List


SPECIAL_CHARS = "!@#$%^&*()-+_"


def first_char_is_zero(nhs_number: str):
    return nhs_number[0] == "0"


def is_numeric(nhs_number: str):
    return nhs_number.isnumeric()


def length_is_10(nhs_number: str):
    return len(nhs_number) == 10


def contains_no_special_chars(nhs_number: str):
    return all([char not in nhs_number for char in SPECIAL_CHARS])


def no_blank_spaces(nhs_number: str):
    return " " not in nhs_number


def validate_nhs_number(nhs_number: str):
    chars_valid = all(
        [
            not first_char_is_zero(nhs_number),
            is_numeric(nhs_number),
            length_is_10(nhs_number),
            contains_no_special_chars(nhs_number),
            no_blank_spaces(nhs_number),
        ]
    )
    if not chars_valid:
        return False

    check_digit = calculate_check_digit(
        digit_sum_division_remainder(digit_multiplication(nhs_number))
    )
    return validate_checkdigit(nhs_number, check_digit)


def digit_multiplication(nhs_number: str) -> List[int]:
    output = []
    for index, number in enumerate(nhs_number):
        if index == len(nhs_number) - 1:
            continue
        multiplication_result = int(number) * (10 - index)
        output.append(multiplication_result)
    return output


def digit_sum_division_remainder(digits: List[int]) -> int:
    return sum(digits) % 11


def calculate_check_digit(remainder: int):
    check_digit = 11 - remainder
    if check_digit == 11:
        return 0
    return check_digit


def validate_checkdigit(nhs_number: str, check_digit: int) -> bool:
    if check_digit == 10:
        return False
    return nhs_number[-1] == str(check_digit)
