def investment(num1, num2):
    investment = float(input("Enter a number: "))
    count = 1
    for wed in range(num1, num2):
        money_added = investment
        percentage = 0.10
        money_added *= 0.10
        investment += money_added


    print(f"Your ROI is {money_added:.2f}, Your new investment is now {investment:.2f} in year{wed}",)
print(investment(1, 31))

