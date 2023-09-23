num = [1,2,3,4,5,6,7,8,9]
odd = 0
even = 0
count = 1
for count in num:

    if count%2 == 0:
        even =+1
    else:
        odd +=1
    count +=1

print(f"Number of even number:{even} ")
print(f"Number of odd number:{odd}  ")
