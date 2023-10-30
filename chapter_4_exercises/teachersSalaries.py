def calculateTeachersSalaries():
    name = input("teachers name: ")
    periods = int(input("no of periods: "))
    rate = 20
    if 0 < periods <= 100:
        gross_salary = periods * rate
    if periods > 100:
        gross_salary = (100 * 20) + (periods - 100) * 25
    return f' Teacher: {name} \n Total periods: {periods} \n Gross salary :$ {gross_salary}'


print(calculateTeachersSalaries())
