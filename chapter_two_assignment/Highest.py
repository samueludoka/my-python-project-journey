number = int(input("Enter a number"))
highest_number = 0
lowest_number =number
for count in range(1,number,1):
	number = int(input("Enter a number"))
	
	if number > highest_number:
		highest_number = number
	if number < highest_number:
		lowest_number = number

		print(highest_number)
		print(lowest_number)