class DisplayEmp:
    def display_emp(self) -> None:
        print("+=============================================================================+")
        print("| {:<8} | {:<20} | {:<14} | {:<10}  | {:<10} |".format("EmpID", "EmpName", "EmpJoinDate", "EmpDept",
                                                                "EmpSalary"))
        print("+=============================================================================+")
        f = open("Employee.txt", 'r')
        lines = f.read().splitlines()

        for line in lines:
            data = line.split(" ")
            print("| {:<8} | {:<20} | {:<14} | {:<10} | {:<10} |".format(data[0], data[1], data[2], data[3],
                                                                    data[4]))
        print("+=============================================================================+")