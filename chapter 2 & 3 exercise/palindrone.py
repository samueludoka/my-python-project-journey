

count = 1


def is_palindrone(number):
    result = count
    returning = 0
    while number != 0:
        value = number % 10
        returning = returning * 10 + value
        number = number // 10
        if returning == result:
            return True
        else:
            return False
print(is_palindrone(121))