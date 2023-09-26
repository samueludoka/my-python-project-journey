gallons = int(input("Enter the gallons used(-1to end): "))
miles = int(input("Enter the miles driven: "))
count = 0
result = 0
total = 0
while gallons != -1:
    total += gallons
    count += 1
    gallons = int(input("Enter the gallons used(-1to end): "))
    miles = int(input("Enter the miles driven: "))
    result = gallons / miles
    print(f"The miles/gallons for this tank was {result}")



