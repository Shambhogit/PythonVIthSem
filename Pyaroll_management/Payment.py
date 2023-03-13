from datetime import date


class Payment:
    def payment(self):
        emp = open("Employee.txt", "r")
        empId = int(input("Enter EMP_ID to Pay Salary : "))
        lines = list(emp.read().splitlines())
        count = 0
        for line in lines:
            data = line.split()

            if int(data[0]) == empId:
                count = count + 1
                print("EMP_ID                      :", data[0])
                print("EMP_NAME                    :", data[1])
                print("EMP_JOINING_DATE            :", data[2])
                print("EMP_DEPARTMENT              :", data[3])
                print("EMP_SALARY                  :", data[4])

                print("==============================================================")
                choice = input("DO YOU WANT TO PAY SALARY : PRESS(Y) : ")
                if choice == 'y' or choice == 'Y':
                    basic = int(data[4])
                    humanResourceAllowance = (basic * 12) // 100
                    travalAllowance = (basic * 8) // 100
                    basicSalary = basic + humanResourceAllowance + travalAllowance
                    incomeTax = (basicSalary * 8) // 100
                    professionalTax = (basicSalary * 5) // 100
                    today = str(date.today())
                    grossPay = basicSalary - incomeTax - professionalTax

                    print("BASIC_SALARY                :  ", basic)
                    print("HUMAN_RESOURCE_ALLOWANCE    : +", humanResourceAllowance)
                    print("TRAVAL_ALLOWANCE            : +", travalAllowance)
                    print("INCOME_TAX                  : -", incomeTax)
                    print("PROFESSIONAL_TAX            : -", professionalTax)
                    print("DATE_TODAY                  :  ", today)
                    print("GROSS_PAY                   :  ", grossPay)

                    choice = input("DO YOU WANT TO CONFIRM PAYMENT PRESS : (Y / y) : ")
                    if choice == 'y' or choice == 'Y':
                        salary = open("Salary.txt", "a")
                        salaryData = data[0] + " " + data[1] + " " + str(basic) + " " + str(
                            humanResourceAllowance) + " " + str(travalAllowance) + " " + str(incomeTax) + " " + str(
                            professionalTax) + " " + str(today) + " " + str(grossPay) + "\n"
                        salary.write(salaryData)
                        print("PAYMENT SUCCESSFUL...!!!")
                        salary.close()
                        emp.close()
                        return
                    else:
                        print("NO CONFIRMATION TO SALARY...!!!")
                        emp.close()
                        return
        if count == 0:
            print("RECORD NOT FOUND...!!!")
            emp.close()
            return
