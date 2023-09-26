import math


def divide_or_square(number: int):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return


print(divide_or_square(225))
