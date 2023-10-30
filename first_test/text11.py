def check_value():
    number = [1, 2, 3, 4, 5]
    specific_value = int(input("Enter the number to check"))
    if specific_value in number:
        print(f"{specific_value} is in number")
    else:
        print(f"{specific_value} is not in number")


