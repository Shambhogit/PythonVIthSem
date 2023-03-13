class AddEmployee:

    def get_last_emp(self)-> int:
        try:
            empFile = open("Employee.txt", 'r')
            line = empFile.read().splitlines()
            last_line = line[-1]
            data = last_line.split(" ")
            lastId = int(data[0])
            return lastId
        except:
            return 1000



    def add_employee(self):

        empFile = open("Employee.txt", 'a')
        if empFile:
            print("===========================================================================================")
            empId = AddEmployee.get_last_emp(self) + 1
            empName = input("Enter Employee Name : ").capitalize()
            while True:
                try:
                    empJoiningDate = input("Enter Employee Joining Date(DD/MM/YYYY) : ")
                    date = empJoiningDate.split("/")
                    size = len(date)
                    day = int(date[0])
                    month = int(date[1])
                    year = int(date[2])
                    if (1 <= day <= 31) and (1 <= month <= 12) and (1950 <= year <= 2100) and size == 3:
                        break
                    else:
                        print("\nYou Enter wrong date !!!")
                except:
                    print("\nYou Enter wrong date !!!")

            departmentName = input("Enter Name of Department : ").capitalize()
            salary = input("Enter Salary of Employee : ")
            print("===========================================================================================")
            line = str(empId)+" "+empName+" "+empJoiningDate+" "+departmentName+" "+salary+"\n"
            empFile.write(line)
            empFile.close()
        else:
            empFile = open("Employee.txt")
            print("File is created now you can insert data")
