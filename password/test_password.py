from password import (
    validate_length,
    validate_number,
    validate_password,
    validate_symbol,
    validate_uppercase,
    validate_lowercase,
)

import unittest


class TestValidatePassword(unittest.TestCase):
    def test_validate_password_returns_true_for_valid(self):
        # Arrange
        input_password = "aA1%lkjlkjlkj"
        expected = True
        # Act
        actual = validate_password(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_uppercase_returns_true_if_valid(self):
        # Arrange
        input_password = "aA1%"
        expected = True
        # Act
        actual = validate_uppercase(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_uppercase_returns_false_if_invalid(self):
        # Arrange
        input_password = "aa1%"
        expected = False
        # Act
        actual = validate_uppercase(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_lowercase_returns_true_if_valid(self):
        # Arrange
        input_password = "aa1%"
        expected = True
        # Act
        actual = validate_lowercase(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_lowercase_returns_false_if_invalid(self):
        # Arrange
        input_password = "AA1%"
        expected = False
        # Act
        actual = validate_lowercase(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_number_returns_true_if_valid(self):
        # Arrange
        input_password = "AA1%"
        expected = True
        # Act
        actual = validate_number(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_number_returns_false_if_invalid(self):
        # Arrange
        input_password = "AA%"
        expected = False
        # Act
        actual = validate_number(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_symbol_returns_true_if_valid(self):
        # Arrange
        input_password = "AA%"
        expected = True
        # Act
        actual = validate_symbol(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_symbol_returns_false_if_invalid(self):
        # Arrange
        input_password = "AA"
        expected = False
        # Act
        actual = validate_symbol(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_length_returns_false_if_invalid(self):
        # Arrange
        input_password = "AA"
        expected = False
        # Act
        actual = validate_length(input_password)
        # Assert
        self.assertEqual(expected, actual)

    def test_validate_length_returns_true_if_valid(self):
        # Arrange
        input_password = "AAlkjlkjlkj"
        expected = True
        # Act
        actual = validate_length(input_password)
        # Assert
        self.assertEqual(expected, actual)
