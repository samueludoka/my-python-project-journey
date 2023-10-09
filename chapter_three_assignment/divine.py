def add_function(number):
    product = 0
    for count in number:
        product += count
    return product


def multiply_function(number):
    product = 1
    for count in number:
        product *= count
    return product


def max_function(number):
    max = 0
    for count in number:
        if count > max: max = count
    return max


def min_function(number):
    minum = number[0]
    for count in number:
        if count < minum:
            minum = count

    return minum

def no_duplicate(numbers):
    list = []
    for count in numbers:
        if count not in list:
            list.append(count)

    return list

def triple_3x(numbers):
    triple = []
    for count in numbers:
        triple *= numbers[count] * numbers[count] * numbers[count]

    return triple
