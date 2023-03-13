class SearchEmployee:
    def search_employee(self):
        try:

            f = open("Employee.txt", "r")

            print('''ENTER OPTION TO SEARCH EMPLOYEE
            1.BY EMP_ID
            2.BY NAME
            3.BY SALARY
            4.BY DEPARTMENT''')
            cho = int(input("Enter your choice : "))
            match cho:
                case 1:
                    empId = input("Enter EMP_ID to search : ")
                    lines = list(f.read().splitlines())
                    count = 0
                    print("+=============================================================================+")
                    print(
                        "| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format("EmpID", "EmpName",
                                                                               "EmpJoinDate", "EmpDept",
                                                                               "EmpSalary"))
                    print("+=============================================================================+")
                    for line in lines:
                        data = line.split(" ")
                        if int(data[0]) == int(empId):
                            count = count + 1
                            print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2],
                                                                                         data[3],
                                                                                         data[4]))
                    print("+=============================================================================+")
                    if count == 0:
                        print("NO RECORD FOUND")

                case 2:
                    name = input("Enter EMP_NAME to Search : ")
                    lines = list(f.read().splitlines())
                    count = 0
                    print("+=============================================================================+")
                    print(
                        "| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format("EmpID", "EmpName",
                                                                               "EmpJoinDate", "EmpDept",
                                                                               "EmpSalary"))
                    print("+=============================================================================+")
                    for line in lines:
                        data = line.split(" ")
                        if data[1].__eq__(name.capitalize()):
                            count = count + 1
                            print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2],
                                                                                         data[3],
                                                                                         data[4]))
                    print("+=============================================================================+")
                    if count == 0:
                        print("NO RECORD FOUND")

                case 3:
                    salary = input("Enter EMP_SALARY to Search : ")
                    lines = list(f.read().splitlines())
                    count = 0
                    print("+=============================================================================+")
                    print(
                        "| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format("EmpID", "EmpName",
                                                                               "EmpJoinDate", "EmpDept",
                                                                               "EmpSalary"))
                    print("+=============================================================================+")
                    for line in lines:
                        data = line.split(" ")
                        if int(data[4]) == int(salary):
                            count = count + 1
                            print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2],
                                                                                         data[3],
                                                                                         data[4]))
                    print("+=============================================================================+")
                    if count == 0:
                        print("NO RECORD FOUND")

                case 4:
                    dept = input("Enter DEPARTMENT to Search : ")
                    lines = list(f.read().splitlines())
                    count = 0
                    print("+=============================================================================+")
                    print(
                        "| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format("EmpID", "EmpName",
                                                                               "EmpJoinDate", "EmpDept",
                                                                               "EmpSalary"))
                    print("+=============================================================================+")
                    for line in lines:
                        data = line.split(" ")
                        if data[3].__eq__(dept.capitalize()):
                            count = count + 1
                            print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2],
                                                                                         data[3],
                                                                                         data[4]))
                    print("+=============================================================================+")
                    if count == 0:
                        print("NO RECORD FOUND")
        except:
            print("SOMETHING WENT WRONG.....!!!!!!")
