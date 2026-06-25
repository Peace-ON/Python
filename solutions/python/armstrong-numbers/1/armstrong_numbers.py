def is_armstrong_number(number):
    number_string = str(number)
    number_digit = len(number_string)
    sum_of_power = sum(pow(int(digit), number_digit) for digit in number_string)
    return sum_of_power == number
