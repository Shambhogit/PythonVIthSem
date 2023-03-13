# def calculategmean(a, b):
#     mean = (a*b) / (a+b)
#     print(mean)
#
# calculategmean(5,1)
# calculategmean(6,4)

def fibo(a):
    m1 = 0
    m2 = 1
    m3 = 0
    for i in range(a-1):
        m3 = m1+m2
        m1 = m2
        m2 = m3
    print(a, "th Fibonacci number is : ", m3)
fibo(10)
