def series(number1, number2):
    count = 1
    for i in range(number1, number2):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzBuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
print(series(1,51))



