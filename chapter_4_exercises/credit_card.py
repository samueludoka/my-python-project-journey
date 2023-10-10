def creditcardNumber(creditCardNumber):
    result = ""
    if creditcardNumber.length >= 13 and creditcardNumber <= 16:
        if creditcardNumber[0] == 4:
            result = "visa card"
        elif creditcardNumber[0] == 5:
            result = "mastercard"
        elif creditcardNumber[0] == 3 and creditcardNumber[1] == 7:
            result = "American Express Card"
        elif creditcardNumber[0] == 6:
            result = "Discovery card"
        else:
            "invalid length"
    return result

def cardValidate(creditCardNumber):
    evenSum = 0
    oddSum = 0
    sum = 0
    digit = 0
    for i in len(creditCardNumber):
        if i % 2 == 0:
            multiply_by_two = digit * 2
            if multiply_by_two > 9:
                mul = multiply_by_two
            evenSum += multiply_by_two
        else:
            oddSum += digit

    sum = evenSum + oddSum
    if sum % 10 == 0:
        print("credit card validity status: valid")
    else:
        print("credit card validity status: invalid")

    sum = True

    return sum % 10 == 0

