result = 0
count = 0
returning = 0
number = int(input('Enter five digits integer: '))
reverse_digit = number
while number != 0:
    value = number % 10
    returning = returning * 10 + value
    number = number // 10
if returning == reverse_digit:
    print('number is palindrone: ')
else:
    print('number is not palindrone: ')


