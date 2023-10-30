students_age = {"dike": 33, "ope": 20, "precious": 27, "joy": 20, "delighted": 22}


def student_age(age):
    name = input("pls enter your name: ").lower()
    for key in students_age.keys():
        if key == name:
            return f"hi,{name} your age is {students_age.get(key)}"
    else:
        while name not in students_age.keys():
            age = int(input("name not found, enter your age: "))
            students_age.update({name: age})
            return f"hi, {name} your age is {students_age.get(name)}"


print(students_age)


def sum_list(number):
    total = 0
    for i in number:
        for j in i:
            total += j
    return total


print(sum_list([[2, 4, 6, 5], [2, 3, 5, 6]]))


def sum_list2(numbers):
    total = 0
    for sikiru in numbers:
        total += sum(sikiru)
    return total


print(sum_list2([[2, 4, 6, 5], [2, 3, 5, 6]]))


def sum_list3(numbers3):
    number0, number1 = numbers3
    total = number0 + number1
    total = sum(total)
    return total


print(sum_list2([[2, 4, 6, 5], [2, 3, 5, 6]]))


def check_list(numbers):
    new_check = []
    for num in numbers:
        if num % 2 != 1:
            new_check.append(num)
    return new_check


print(set(check_list([1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14])))
