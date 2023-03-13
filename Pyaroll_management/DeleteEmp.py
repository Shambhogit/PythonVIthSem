class DeleteEmp:
    def delete_employee(self):
        print("===========================================================================================")
        id = int(input("Enter Id of Employee to Delete Record : "))
        f = open("Employee.txt", "r")
        lines = f.read().splitlines()
        count = 0
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
                choice = input("DO YOU WANT TO DELETE THIS RECORD : PRESS (Y)\n")
                if choice == 'Y' or choice == 'y':
                    del lines[count]
                    f = open("Employee.txt", "w")
                    for line1 in lines:
                        f.write(line1 + "\n")
                    f.close()
                    print("===========================================================================================")
                    print("!!!...RECORD DELETED SUCCESSFULLY...!!!")
                    return
                else:
                    print("===========================================================================================")
                    print("!!!...RECORD NOT DELETED...!!!")
                    return
            count = count+1
        print("===========================================================================================")
        print("NO RECORD FOUND FOR GIVEN EMP_ID")

