def series(number):
    x = 0
    y = 1
    sumz = x + y
    while x < number:
        print(x, end=' ')
        x = y
        y = sumz
        sumz = x + y
print(series(50))

