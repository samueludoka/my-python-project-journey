num = int(input("Enter a number: "))
total = 1
constant = 1.0
for count in range(num):
    count += 2
    total = total + count
    constant += 4 - 4 / total * count
print(constant)
