import csv
from typing import List


def csv_():
    with open("Jan_2020.csv") as csv_file:
        return list(csv.reader(csv_file, delimiter=","))


def get_col_as_list(input_matrix, index):
    return [row[index] for row in input_matrix]


def count_two_column_match_input_1(
    input_matrix, col_1_index, col_1_match, col_2_index, col_2_match
):
    count = 0
    for row in input_matrix:
        if row[col_1_index] == col_1_match and row[col_2_index] == col_2_match:
            count = count + 1
    return count


def count_two_column_match_input(
    input_matrix, col_1_index, col_1_match, col_2_index, col_2_match
):
    return sum(
        [
            1
            if row[col_1_index] == col_1_match and row[col_2_index] == col_2_match
            else 0
            for row in input_matrix
        ]
    )


def count_two_column_match_input_list(
    input_matrix, col_1_index, col_1_match, col_2_index, col_2_match
):
    return sum(
        [
            1
            if row[col_1_index] in col_1_match and row[col_2_index] in col_2_match
            else 0
            for row in input_matrix
        ]
    )


def delayed_flights_from_ny():
    print(count_two_column_match_input_list(csv_(), 12, ["JFK", "LGA", "EWR"], -7, "1"))


if __name__ == "__main__":
    delayed_flights_from_ny()
    # main()

x = [
    "DAY_OF_MONTH",
    "DAY_OF_WEEK",
    "OP_UNIQUE_CARRIER",
    "OP_CARRIER_AIRLINE_ID",
    "OP_CARRIER",
    "TAIL_NUM",
    "OP_CARRIER_FL_NUM",
    "ORIGIN_AIRPORT_ID",
    "ORIGIN_AIRPORT_SEQ_ID",
    "ORIGIN",
    "DEST_AIRPORT_ID",
    "DEST_AIRPORT_SEQ_ID",
    "DEST",
    "DEP_TIME",
    "DEP_DEL15",
    "DEP_TIME_BLK",
    "ARR_TIME",
    "ARR_DEL15",
    "CANCELLED",
    "DIVERTED",
    "DISTANCE",
]
