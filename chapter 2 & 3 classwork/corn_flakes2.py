name = input("Enter name of item: ")
price = int(input("Enter price: "))
Discount = int(input("Enter discount in %: "))
deposit = int(input ("Enter deposit: "))
score = bool(input("Enter true or false for credit score status: "))
discount = price * 0.10
print(f'discount is {discount}')
if score == True:
    downpayment = 0.25 *price
    print(f'payment is {downpayment}')
if score == False:
    downpayment1 = 0.10 * price
    print(f'payment is {downpayment1}')
