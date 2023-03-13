# write a python function that takes a number as a
# parameter and check the number is prime of not
def check_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print("Entered number is prime number")
    else:
        print("Entered number is not prime number")


check_prime(int(input("Enter any number: ")))

