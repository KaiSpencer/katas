from spin_words import spin_words
import unittest


class TestSpinWords(unittest.TestCase):
    def test_spin_words(self):
        # Arrange
        words = "Hey fellow warriors"
        expected = "Hey wollef sroirraw"
        # Act
        actual = spin_words(words)
        # Assert
        self.assertEqual(expected, actual)
