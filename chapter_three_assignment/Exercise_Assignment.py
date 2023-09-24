def series(number):
    for n in range(number):
        if n != 6 and n != 3:
            print(n, end="\t")
print(series(10))