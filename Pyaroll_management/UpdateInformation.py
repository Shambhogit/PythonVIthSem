class UpdateInformation:

    def update_information(self):
        print("===========================================================================================")
        id = int(input("Enter Id of Employee to Update Record : "))
        f = open("Employee.txt", "r")
        lines = f.read().splitlines()
        count = 0
        updated_line = ""
        for line in lines:
            data = line.split(" ")
            if int(data[0]) == id:
                print("+=============================================================================+")
                print(
                    "| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format("EmpID", "EmpName", "EmpJoinDate", "EmpDept",
                                                                           "EmpSalary"))
                print("+=============================================================================+")
                print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2], data[3],
                                                                             data[4]))
                print("+=============================================================================+")
                choice = input("DO YOU WANT TO UPDATE THIS RECORD : PRESS (Y)\n")
                if choice == 'Y' or choice == 'y':
                    print('''WHAT DO YOU WANT TO UPDATE
                    1.NAME
                    2.JOINING DATE
                    3.DEPARTMENT
                    4.SALARY''')

                    cho = int(input("Enter your choice : "))
                    match cho:
                        case 1:
                            data[1] = input("Enter Updated EMP_NAME : ")
                            data[2] = data[2]
                            data[3] = data[3]
                            data[4] = data[4]
                        case 2:
                            data[1] = data[1]
                            data[2] = input("Enter Updated EMP_JOINING_DATE : ")
                            data[3] = data[3]
                            data[4] = data[4]
                        case 3:
                            data[1] = data[1]
                            data[2] = data[2]
                            data[3] = input("Enter Updated EMP_DEPT : ")
                            data[4] = data[4]
                        case 4:
                            data[1] = data[1]
                            data[2] = data[2]
                            data[3] = data[3]
                            data[4] = input("Enter Updated EMP_SALARY : ")
                        case _:
                            print("!!!...ENTER VALID CHOICE...!!!")

                    print("+=============================================================================+")
                    print("!!!...DATA UPDATED SUCCESSFULLY...!!!")
                    updated_line = data[0]+" "+data[1]+" "+data[2]+" "+data[3]+" "+data[4]
                    lines[count] = updated_line
                    f = open("Employee.txt", "w")
                    for line1 in lines:
                        f.write(line1 + "\n")
                    f.close()
                else:
                    return
            count = count + 1
        print("===========================================================================================")
        print("NO RECORD FOUND FOR GIVEN EMP_ID")



