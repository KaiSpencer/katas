import unittest

from parameterized import parameterized

from validate import (
    is_longer_than_253_chars,
    more_than_127_levels,
    valid_characters,
    all_levels_not_start_or_end_with_hyphen,
    all_levels_not_longer_than_63_char,
    is_top_level_domain_fully_numeric,
    is_enough_subdomains,
    validate,
)


class TestValidate(unittest.TestCase):
    @parameterized.expand(
        [
            ("codewars", False),
            ("g.co", True),
            ("codewars.com", True),
            ("CODEWARS.COM", True),
            ("sub.codewars.com", True),
            ("codewars.com-", False),
            (".codewars.com", False),
            ("example@codewars.com", False),
            ("127.0.0.1", False),
        ]
    )
    def test_validate(self, domain, expected):
        # Arrange / Act
        actual = validate(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_longer_than_253_chars(self):
        # Arrange
        expected = True
        domain = "".join([str(x) for x in range(254)])
        # Act
        actual = is_longer_than_253_chars(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_not_longer_than_253_chars(self):
        # Arrange
        expected = False
        domain = ""
        # Act
        actual = is_longer_than_253_chars(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_more_than_127_levels(self):
        # Arrange
        expected = True
        domain = "".join(["x." for _ in range(127)])
        # Act
        actual = more_than_127_levels(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_not_more_than_127_levels(self):
        # Arrange
        expected = False
        domain = "".join(["x." for _ in range(126)])
        # Act
        actual = more_than_127_levels(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_valid_characters(self):
        # Arrange
        expected = True
        domain = "asd"
        # Act
        actual = valid_characters(domain)
        # Assert
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [("asd", True), ("asd%", False), ("asdfg.s.s.££", False), ("a.a-a.a", True)]
    )
    def test_valid_characters_(self, domain, expected):
        # Arrange / Act
        actual = valid_characters(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_all_levels_not_start_or_end_with_hyphen_false(self):
        # Arrange
        expected = False
        domain = "-a-test-.com"
        # Act
        actual = all_levels_not_start_or_end_with_hyphen(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_all_levels_not_start_or_end_with_hyphen_true(self):
        # Arrange
        expected = True
        domain = "a-test.sllsl.lslsl.l.com"
        # Act
        actual = all_levels_not_start_or_end_with_hyphen(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_all_levels_not_longer_than_63_char_true(self):
        # Arrange
        expected = True
        domain = "a-test.sllsl.lslsl.l.com"
        # Act
        actual = all_levels_not_longer_than_63_char(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_all_levels_not_longer_than_63_char_false(self):
        # Arrange
        longer = "".join("x" for _ in range(64))
        expected = False
        domain = f"{longer}.{longer}.lslsl.l.com"
        # Act
        actual = all_levels_not_longer_than_63_char(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_top_level_domain_fully_numeric_false(self):
        # Arrange
        expected = False
        domain = f"example.123a"
        # Act
        actual = is_top_level_domain_fully_numeric(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_top_level_domain_fully_numeric_true(self):
        # Arrange
        expected = True
        domain = f"example.123"
        # Act
        actual = is_top_level_domain_fully_numeric(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_enough_subdomains_true(self):
        # Arrange
        expected = True
        domain = f"avc.example123"
        # Act
        actual = is_enough_subdomains(domain)
        # Assert
        self.assertEqual(expected, actual)

    def test_is_enough_subdomains_false(self):
        # Arrange
        expected = False
        domain = f"example123"
        # Act
        actual = is_enough_subdomains(domain)
        # Assert
        self.assertEqual(expected, actual)
