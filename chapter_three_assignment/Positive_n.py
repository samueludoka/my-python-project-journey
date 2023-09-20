sam = 0
positive_number = 0
negative_number = 0
count = 0
zero = 0
for count in range(1,sam,1):
	num = int(input("Enter a range of number and enter 000 to stop the count: "))
	if(num > 0):
		print("positive numbers")
	elif(num > 0):
		print("Negative numbers")
	else:
		print("Equal to zero")
		positive_number += count
		print("Positive_number")
		negative_number += count
		print("negative_number")
		