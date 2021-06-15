from typing import AbstractSet
import unittest
from who_likes_it import who_likes_it


class TestWhoLikesIt(unittest.TestCase):
    def test_nobody_likes(self):
        # Arrange
        expected = "no one likes this"
        likes_it = []
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)

    def test_one_likes(self):
        # Arrange
        expected = "Jeff likes this"
        likes_it = ["Jeff"]
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)

    def test_two_likes(self):
        # Arrange
        expected = "Jeff and Bob like this"
        likes_it = ["Jeff", "Bob"]
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)

    def test_three_likes(self):
        # Arrange
        expected = "Jeff, Bob and Tim like this"
        likes_it = ["Jeff", "Bob", "Tim"]
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)

    def test_more_than_three_likes(self):
        # Arrange
        expected = "Jeff, Bob and 2 others like this"
        likes_it = ["Jeff", "Bob", "Tim", "Ben"]
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)

    def test_more_than_three_likes_1(self):
        # Arrange
        expected = "Jeff, Bob and 5 others like this"
        likes_it = ["Jeff", "Bob", "Tim", "Ben", "", "", ""]
        # Act
        actual = who_likes_it(likes_it)
        # Assert
        self.assertEqual(expected, actual)
