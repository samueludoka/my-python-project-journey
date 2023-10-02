
number_two = 2
for row in range(1, 13):
    for column in range(1, 21):
        print(f"{column:2}*{row:2}={column*row:2}\t", end="")
    print("")
