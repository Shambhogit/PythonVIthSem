# write a program that reads marks of three quizzes and outputs the total out of 100

quizze_one = int(input("Enter any number between 1 to 100 : "))
if quizze_one > 100 and quizze_one < 0:
    print("Your input is incorrect please re-enter")
    quizze_one = int(input("Enter any number between 1 to 100 : "))

quizze_two = int(input("Enter any even number between 1 to 100 : "))
if quizze_two%2 != 0 :
    print("Your input is incorrect please re-enter")
    quizze_two = int(input("Enter even number between 1 to 100 : "))

quizze_three = int(input("Enter any odd number between 1 to 100 : "))
if quizze_three%2 == 0:
    print("Your input is incorrect please re-enter")
    quizze_three = int(input("Enter even number between 1 to 100 : "))

print("avrege you get is : ", (quizze_one + quizze_two + quizze_three)/3)
