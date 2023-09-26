num = int(input("Enter a number: "))
fact = 1
e = 1.0
total = 1
for count in range(num):
    count += 1
    fact = fact * count
    e += 1 / fact*count
print(e)
