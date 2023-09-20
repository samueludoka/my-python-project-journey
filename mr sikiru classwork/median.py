number1 = [10,20,15,25,5,30,35,20,10,20]
kop=[]

for i in range(len(number1)):
    kop.append(min(number1))
    number1.remove(min(number1))
    print(kop)
