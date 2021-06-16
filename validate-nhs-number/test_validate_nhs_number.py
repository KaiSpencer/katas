import unittest

from parameterized import parameterized

from validate_nhs_number import (
    does_not_start_with_0,
    is_nhs_number_valid,
    no_alphabetic_characters,
    is_10_chars,
    no_special_characters,
    no_blank_spaces,
)


class TestHelloWorld(unittest.TestCase):
    def test_does_not_start_with_0_returns_true_if_not_0(self):
        # Arrange
        nhs_number = "123456789"
        expected = True
        # Act
        actual = does_not_start_with_0(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_does_not_start_with_0_returns_false_if_0(self):
        # Arrange
        nhs_number = "023456789"
        expected = False
        # Act
        actual = does_not_start_with_0(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_alphabetic_characters_returns_true_if_no_alphabetic(self):
        # Arrange
        nhs_number = "023456789"
        expected = True
        # Act
        actual = no_alphabetic_characters(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_alphabetic_characters_returns_falsee_if_contains_alphabetic(self):
        # Arrange
        nhs_number = "s23456789"
        expected = False
        # Act
        actual = no_alphabetic_characters(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_10_chars_returns_true_if_10(self):
        # Arrange
        nhs_number = "0123456789"
        expected = True
        # Act
        actual = is_10_chars(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_10_chars_returns_false_if_not_10(self):
        # Arrange
        nhs_number = "01234567899"
        expected = False
        # Act
        actual = is_10_chars(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_special_characters_returns_true_if_no_special_characters(self):
        # Arrange
        nhs_number = "01234567899"
        expected = True
        # Act
        actual = no_special_characters(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_special_characters_returns_false_if_contains_special_characters(self):
        # Arrange
        nhs_number = "*1234567899"
        expected = False
        # Act
        actual = no_special_characters(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_blank_spaces_returns_true_if_no_blank_spaces(self):
        # Arrange
        nhs_number = "*1234567899"
        expected = True
        # Act
        actual = no_blank_spaces(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    def test_no_blank_spaces_returns_false_if_blank_spaces(self):
        # Arrange
        nhs_number = "*12345 7899"
        expected = False
        # Act
        actual = no_blank_spaces(nhs_number)
        # Assert
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            ("0", False),
            ("asd", False),
            ("1123456789", True),
            ("**********", False),
            ("1234567 99", False),
        ]
    )
    def test_is_nhs_number_valid(self, nhs_number, expected):
        # Arrange / Act
        actual = is_nhs_number_valid(nhs_number)
        # Assert
        self.assertEqual(expected, actual)
