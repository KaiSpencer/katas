def roman_to_int(s: str):
    numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, numeral in enumerate(s):
        print("i", i)
        if i < len(s) - 1:
            if numerals[numeral] < numerals[s[i + 1]]:
                print(numerals[numeral])
                print(numerals[s[i + 1]])

                total += numerals[s[i + 1]] - numerals[numeral]
                print("total:", total)
                continue
        total += numerals[numeral]

    return total
