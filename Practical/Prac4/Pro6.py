# write a program that takes the marks of 5 subjects and displays the grade
print("please enter marks between 0 to 100")
marathi = int(input("Enter the marks of Marathi: "))
hindi = int(input("Enter the marks of Hindi: "))
math = int(input("Enter the marks of Math: "))
english = int(input("Enter the marks of English: "))
history = int(input("Enter the marks of History: "))

if (0 < marathi > 100) or\
        (0 < hindi > 100) or (0 < math > 100) \
        or (0 < english > 100) or (0 < history > 100):
    print("You enter some wrong input")

else:
    perc = (marathi + hindi + math + history + english) / 5
    if 35 <= perc < 45:
        print("Pass")
    elif 45 <= perc < 60 :
        print("Grade C")
    elif 60 <= perc < 75:
        print("Grade B")
    elif 75 <= perc < 85:
        print("Grade A")
    elif 85 <= perc <= 100:
        print("Grade A with distinction")
    else:
        print("Fail")