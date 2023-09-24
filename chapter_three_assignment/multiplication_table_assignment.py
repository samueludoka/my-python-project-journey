def multiplication_table(number1, number2):
    number_two = 2
    for row in range(number1, number2):
        for column in range(1, 21):
            print(f"{column:2}*{row:2}={column*row:2}\t", end="")
        print("")
print(multiplication_table(1, 13))
