def list_numbers(score):
    numbers = []
    for i in range(1, 21):
        numbers.append(i)
    return numbers


def scores_odd(score):
    numbers = []
    for i in range(1, 21, ):
        numbers.append(i)
        if i % 2 != 0:
            i = numbers
    return numbers


def double_odd_numbers(score):
    numbers = []
    for i in range(1, 21, ):
        numbers.append(i)
        if i % 2 != 0:
            i = numbers
    return numbers * 2


def double_odd_number(number):
    if number % 2 == 1:
        return number


# def double_odd_check(score):
#     return list(filter(lambda, number))


def change_some_elements(score):
    numbers = []
    for i in range(1, 21, 2):
        numbers.append(i)
        if i % 2 != 0:
            i = numbers
            integer = numbers * 2
            num = []
            count = 4
            for count in integer:
                count += 1
                if count == 8:
                    break
    return num
