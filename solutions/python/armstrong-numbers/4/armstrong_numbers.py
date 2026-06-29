def is_armstrong_number(number):
    number_string = str(number)
    number_digit = len(number_string)
    return number == sum(int(digit) ** number_digit for digit in number_string)