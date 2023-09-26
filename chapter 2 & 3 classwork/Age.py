#age = int(input("Enter an age"))
#if age < 18:
 #   print("you are not eligible to enter our club....")
#else:
 #   print("Eligible")
#result = "not Eligible" if age < 18 else "Eligible"
# line 6 is known as teanary operator in java and python, and its used when there are two conditions
#print(result)
# import random




#if age < 18:
 #   print("you are not eligible to enter our club...")
#elif age >= 18 and age <= 60:
 #   print("Eligible")
#else:
 #   "not eligible"




# language = input("Enter your language")
# match language:
#     case "Yoruba":
#         print("Welcome to ibadan")
#     case "ibo":
#         print("Welcome to anambra")
#     case "hausa":
#         print("welcome to kano")
#     case _:
#         print("You are not from here")





# score = int(input("Enter your score"))
# result = ""
# if score > 70:
#     if score > 90:
#         result = "pass with distinctions"
# else:
#     result = "fail"
# print(result)


# score = int(input("Enter your score"))
# result = ""
# if score > 90 and score <= 100:
#         result = "Distinction"
# elif 80 <= score < 90:
#         result = "Excellent"
# elif score >= 70 and score < 80:
#         result = "B grade"
# elif score >= 60 and score < 70:
#         result = "C grade"
# elif score >= 50 and score < 60:
#         result = "D grade"
# elif score < 50:
#         result = "Fail, come back next time"
# print(f'your score is {score}\n and your result is {result}')





#
# name = input("Enter your name: ")
# if name:
#     print(f"your name is {name}")
# else:
#     print("no name entered")



#
# count = 0
# while count < 10:
#     print (random.randint(1, 21))
#     count += 1
#



#
# count = 0
# while count < random.randint(1, 10):
#     num = input("Enter a number")
#     print("invalid number, try and enter correct number")
#     count += 1
#

#
# guessed_number = random.randint(1,10)
# print(guessed_number)
# guess = int(input("Enter your guess number: "))
# while guessed_number != guess:
#     guess = int(input("Enter your guess number: "))
# count = 1
# sum = 0
# average = 0
# # number = int(input('Enter a number: '))
# while count <= 2 :
#     number = int(input('Enter a number: '))
#     sum = sum + number
#
# average = sum / 10
# print(average)


count = 1
total = 0
while count <= 10:
    score = int(input("Enter student score: "))
    total += score
    count += 1
average = total / count
print(f"the total of scores by the student is {total} \ the average score is {average}")

#
# count = 0
# total = 0
# score = int(input("Enter score: "))
# while score != 00:
#
#     total += count
#     count =+ 1
#     score = int(input("Enter score: "))
# average = total / count
# print(f"the average is {average}")

 # for c in "sikiru":
 #     print(c, "*")


# for i in range(10):
#     print(i+5)
