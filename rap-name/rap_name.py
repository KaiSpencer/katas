import math

NUMBER_CONVERSION = {
    0: "0ero",
    1: "1ne",
    2: "2wo",
    3: "3hree",
    4: "4our",
    5: "5ive",
    6: "6ix",
    7: "7even",
    8: "8ight",
    9: "9ine",
}


def calculate_day_ints(input_date: str) -> tuple:
    date_list = [int(x) for x in str(input_date) if x != "."]
    day = math.ceil((date_list[0] + date_list[1]) / 2)
    year = math.ceil((date_list[-1] + date_list[-2]) / 2)
    return day, year


def calculate_rap_name(input_date):
    day, year = calculate_day_ints(input_date)
    return f"{NUMBER_CONVERSION[day]} {NUMBER_CONVERSION[year]}"
