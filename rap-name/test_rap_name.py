import unittest

from parameterized import parameterized

from rap_name import calculate_day_ints, calculate_rap_name


class TestRomanNumeral(unittest.TestCase):
    def test_calculate_day_ints(self):
        # Arrange
        input_date = "08.01.22"
        expected = 4, 2
        # Act
        actual = calculate_day_ints(input_date)
        # Assert
        self.assertEquals(expected, actual)

    def test_returns_correct_rap_name(self):
        # Arrange
        input_date = "08.01.22"
        expected = "4our 2wo"
        # Act
        actual = calculate_rap_name(input_date)
        # Assert
        self.assertEquals(expected, actual)

    @parameterized.expand(
        [
            ("08.01.22", "4our 2wo"),
            ("11.01.20", "1ne 1ne"),
            ("19.11.29", "5ive 6ix"),
            ("29.11.00", "6ix 0ero"),
        ]
    )
    def test_returns_correct_rap_name_expand(self, input_date, expected):
        # Arrange/Act
        actual = calculate_rap_name(input_date)
        # Assert
        self.assertEquals(expected, actual)