number = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
for i in range(0, len(number)):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
print(number)
l = len(number)
if l % 2 == 1:
    m1 = number[l // 2]
    m2 = number[(l // 2) - 1]
    mid = (m1 + m2) / 2
else:
    mid = number[l // 2]

print(mid)
sum = 0
number = [10,20,15,25,5,30,35,20,10,20]
for k in number:
    sum += k
    mean = sum / l
print(mean)
