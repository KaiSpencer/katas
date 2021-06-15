import unittest

from flights import (
    get_col_as_list,
    count_two_column_match_input,
    count_two_column_match_input_list,
)


class TestFlights(unittest.TestCase):
    def test_get_col_as_list_1(self):
        # Arrange
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index = 1
        expected = [2, 5, 8]
        # Act
        actual = get_col_as_list(input_matrix, index)
        # Assert
        self.assertEquals(expected, actual)

    def test_get_col_as_list_2(self):
        # Arrange
        input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        index = 0
        expected = [1, 4, 7]
        # Act
        actual = get_col_as_list(input_matrix, index)
        # Assert
        self.assertEquals(expected, actual)

    def test_count_two_column_match_input(self):
        # Arrange
        input_matrix = [[1, 2], [1, 2], [1, 2], [0, 1]]
        col_1_index = 0
        col_1_match = 1
        col_2_index = 1
        col_2_match = 2
        expected = 3
        # Act
        actual = count_two_column_match_input(
            input_matrix, col_1_index, col_1_match, col_2_index, col_2_match
        )
        # Assert
        self.assertEquals(expected, actual)

    def test_count_two_column_match_input_list(self):
        # Arrange
        input_matrix = [[1, 2], [1, 2], [1, 2], [0, 1]]
        col_1_index = 0
        col_1_match = [1, 2]
        col_2_index = 1
        col_2_match = [2, 4]
        expected = 3
        # Act
        actual = count_two_column_match_input_list(
            input_matrix, col_1_index, col_1_match, col_2_index, col_2_match
        )
        # Assert
        self.assertEquals(expected, actual)
