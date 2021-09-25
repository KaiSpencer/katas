import unittest

import validate_nhs_number as sut


class TestValidateNhsNumber(unittest.TestCase):
    def test_first_char_is_zero_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "0123123123"
        # Act
        actual = sut.first_char_is_zero(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_first_char_is_zero_returns_false(self):
        # Arrange
        expected = False
        nhs_number = "123123123"
        # Act
        actual = sut.first_char_is_zero(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_numeric_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "123123123"
        # Act
        actual = sut.is_numeric(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_numeric_returns_false(self):
        # Arrange
        expected = False
        nhs_number = "12a3123123"
        # Act
        actual = sut.is_numeric(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_length_is_10_returns_false(self):
        # Arrange
        expected = False
        nhs_number = "12"
        # Act
        actual = sut.length_is_10(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_length_is_10_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "1234567890"
        # Act
        actual = sut.length_is_10(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_contains_no_special_chars_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "1234567890"
        # Act
        actual = sut.contains_no_special_chars(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_contains_no_special_chars_returns_false(self):
        # Arrange
        expected = False
        nhs_number = "*"
        # Act
        actual = sut.contains_no_special_chars(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_blank_spaces_returns_false(self):
        # Arrange
        expected = False
        nhs_number = "*  *"
        # Act
        actual = sut.no_blank_spaces(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_blank_spaces_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "**"
        # Act
        actual = sut.no_blank_spaces(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_nhs_number_returns_true(self):
        # Arrange
        expected = True
        nhs_number = "1231231238"
        # Act
        actual = sut.validate_nhs_number(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_nhs_number_returns_false(self):
        # Arrange
        expected = False
        nhs_number = " *s"
        # Act
        actual = sut.validate_nhs_number(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_digit_multiplication_returns_correct_list(self):
        # Arrange
        expected = [10, 18, 24, 28, 30, 30, 28, 24, 18]
        nhs_number = "1234567890"
        # Act
        actual = sut.digit_multiplication(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_digit_sum_division_remainder_returns_correct(self):
        # Arrange
        expected = 1
        multiplication_list = [10, 18, 24, 28, 30, 30, 28, 24, 18]
        # Act
        actual = sut.digit_sum_division_remainder(multiplication_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_calculate_check_digit_standard_case(self):
        # Arrange
        expected = 8
        remainder = 3
        # Act
        actual = sut.calculate_check_digit(remainder)
        # Assert
        self.assertEqual(expected, actual)

    def test_calculate_check_digit_11_substitution(self):
        # Arrange
        expected = 0
        remainder = 0
        # Act
        actual = sut.calculate_check_digit(remainder)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_checkdigit_returns_true(self):
        # Arrange
        nhs_number = "1231231231"
        check_digit = 1
        expected = True
        # Act
        actual = sut.validate_checkdigit(nhs_number, check_digit)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_checkdigit_returns_false_no_match(self):
        # Arrange
        nhs_number = "1231231232"
        check_digit = 1
        expected = False
        # Act
        actual = sut.validate_checkdigit(nhs_number, check_digit)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_checkdigit_returns_false_check_digit_10(self):
        # Arrange
        nhs_number = "1231231231"
        check_digit = 10
        expected = False
        # Act
        actual = sut.validate_checkdigit(nhs_number, check_digit)
        # Assert
        self.assertEqual(expected, actual)
