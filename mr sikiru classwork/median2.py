number = [10,20,15,25,5,30,35,20,10,20]
count = +1
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i]> number [j]:
            number[i],number[j]=number[j],number[i]
            # median = number / count
print(number)