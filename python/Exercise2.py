import time

t = time.strftime('%H%M')

if int(t) < 1200:
    print("good morning sir")
elif int(t) < 4000:
    print("good afternoon sir")
else:
    print("Good evening sir")
