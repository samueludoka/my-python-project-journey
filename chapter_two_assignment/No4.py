num1 = int(input('Enter first number:'))
num2 = int(input('Enter second  number:'))
num3 = int(input('Enter third number:'))

sum = num1 + num2 + num3
print(sum)

average = num1 + num2 + num3 / 3
print(average)

product = num1 * num2 * num3
print(product)

if num1 < num2 and num3:
	print('num1 is the smallest number')
if num2 < num1 and num3:
	print('num2 is the smallest number')
if num3 < num1 and num2:
	print('num3 is the smallest number')

if num1 > num2 and num3:
	print('num1 is the highest number')
if num2 > num1 and num3:
	print('num2 is the highest number')
if num3 > num1 and num2:
	print('num3 is the highest number')

# this condition is wrong, pls refactor
