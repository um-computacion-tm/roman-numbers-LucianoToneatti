
import unittest

def decimal_to_roman(decimal):
    total= ''
    if decimal >= 100:
        centena = decimal // 100
        if centena <= 3:
            total = 'C' * centena
        elif centena == 4:
            total = 'C' + 'D'
        elif centena >= 5 and centena <= 8:
            resto = centena % 5
            total = 'D' + 'C' * resto
        elif centena == 9:
            total = 'C' + 'M'
        else:
            total = 'M'
        decimal = decimal % 100
        decena = decimal // 10
        if decena <= 3:
            total += 'X' * decena
        elif decena == 4:
            total += 'X' + 'L'
        elif decena >= 5 and decena <= 8:
            resto = decena % 5
            total += 'L' + 'X' * resto
        elif decena == 9:
            total += 'X' + 'C'
        unidad = decimal % 10
        if unidad <= 3:
            total += 'I' * unidad
        elif unidad >= 5 and unidad <= 8:
            resto = unidad % 5
            total += 'V' + 'I' * resto
        elif unidad == 9:
            total += 'I' + 'X'
    elif decimal >= 10:
        decimal = decimal % 100
        decena = decimal // 10
        if decena <= 3:
            total += 'X' * decena
        elif decena == 4:
            total += 'X' + 'L'
        elif decena >= 5 and decena <= 8:
            resto = decena % 5
            total += 'L' + 'X' * resto
        elif decena == 9:
            total += 'X' + 'C'
        unidad = decimal % 10
        if unidad <= 3:
            total += 'I' * unidad
        elif unidad >= 5 and unidad <= 8:
            resto = unidad % 5
            total += 'V' + 'I' * resto
        elif unidad == 9:
            total += 'I' + 'X'
    elif decimal < 10:
        if decimal <= 3:
            total = 'I' * decimal
        elif decimal == 4:
            total = 'I' + 'V'
        elif decimal >= 5 and decimal <= 8:
            resto = decimal % 5
            total = 'V' + 'I' * resto
        elif decimal == 9:
            total = 'I' + 'X'
    return total


def roman_to_decimal(roman):
    number = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    total = 0
    for letter in range(len(roman)):
        if letter > 0 and number[roman[letter]] > number[roman[letter - 1]]:
            total = -number[roman[letter - 1]]
            total += number[roman[letter]]
        else:
            total += number[roman[letter]]
    return total


if __name__ == '__main__':
    unittest.main()