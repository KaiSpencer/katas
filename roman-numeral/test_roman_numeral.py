import unittest
import roman_numeral

from parameterized import parameterized


class TestRomanNumeral(unittest.TestCase):
    @parameterized.expand([("III", 3), ("IV", 4), ("IX", 9)])
    def test_romano_to_int(self, roman, expected):
        actual = roman_numeral.roman_to_int(roman)

        self.assertEquals(expected, actual)
