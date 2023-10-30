def biggestOdd(numbers):
    numbers = '23569'
    odd_numbers = []
    for i in numbers:
        if int(i) % 2 != 0:
            odd_numbers.append(i)
    highest = odd_numbers[0]
    for j in odd_numbers:
        if highest < j:
            highest = j
    return highest

def bigger_odds(numbers):
    # return int(max([numbers for number in numbers if int(number) % 2 == 1]))
    return int(max(filter(lambda n: int(n) % 2 == 1, numbers)))