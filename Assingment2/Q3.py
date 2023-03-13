amount = int(input("Enter amount: "))
notes = 0
if amount >= 2000:
    notes = amount//2000
    amount = amount % 2000
    print("2000 : ", notes)
if amount >= 500:
    notes = amount//500
    amount = amount % 500
    print("500  : ", notes)
if amount >= 200:
    notes = amount//200
    amount = amount % 200
    print("200  : ", notes)

if amount >= 100:
    notes = amount//100
    amount = amount % 100
    print("100  : ", notes)

if amount >= 50:
    notes = amount//50
    amount = amount % 50
    print("50   : ", notes)

if amount >= 10:
    notes = amount//10
    amount = amount % 10
    print("10   : ", notes)

if amount >= 5:
    notes = amount // 5
    amount = amount % 5
    print("5    : ", notes)
if amount >= 1:
    notes = amount//1
    print("1    : ", notes)