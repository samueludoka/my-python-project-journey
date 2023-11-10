with open("demo.txt", mode='w') as file:
    file.write("ope is short girl\n")
    file.write("uye is man beater\n")
    file.write("tobi is sweet husband to ope")

with open('demo.txt', mode='r') as file:
    for record in file:
        Name, Age, Colour, *Others = record.split()
        print(f'{Name:<10}{Age:<10}{Colour:>10}')

try:
    with open("demo1.txt", mode='r') as datas:
        for data in datas:
            a, *b = data.split()
            print(a, *b)

except FileNotFoundError:
    print("make sure you check to your file spelling")
print("program execution continues...")

try:
    age = int(input("Enter ya age: "))
    result = 10 / age
    print(result)
except (ZeroDivisionError, ValueError):
    print("ur age cannot be string literals")
finally:
    print("finally block runs either there is an exception")


def age_check(n):
    if n <= 0:
        raise ValueError("age cannot be equal to or less than zero")
    return f'you are {n} years old'


print(age_check(-2))
