name = input("Enter ur name: ")
Hours_worked = int(input("Enter hours worked: "))
Pay_rate = float(input("Enter pay rate: "))
gross_pay = float(input("Enter gross payment: "))

federal_withholding = 0.20 * gross_pay
federal = gross_pay - federal_withholding
print(f'federal withholding is{federal}')

state_withholding = 0.0877 * gross_pay
state = gross_pay - state_withholding
print(f'state withholding{state}')

net_pay = gross_pay - federal_withholding - state_withholding
print(f'net pay is {net_pay}')


