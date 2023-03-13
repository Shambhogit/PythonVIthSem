class SalaryTable:
    def print_salary_table(self):
        print(
            "+====================================================================================================================================+")
        print("| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("EMP_ID",
                                                                                                          "EMP_NAME",
                                                                                                          "BASIC_SALARY",
                                                                                                          "HRA",
                                                                                                          "TRAVAL_ALLOWANCE",
                                                                                                          "INCOME_TAX",
                                                                                                          "PROFESSIONAL_TAX",
                                                                                                          "PAYMENT_DATE",
                                                                                                          "GROSS_PAY"))
        print(
            "+====================================================================================================================================+")

        salary = open("Salary.txt", "r")
        lines = salary.read().splitlines()
        for line in lines:
            data = line.split()
            print(
                "| {:<10} | {:<10} | {:<10}   | {:<10} | {:<10}       | {:<10} | {:<10}       | {:<10}   | {:<10} |".format(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8]))
        print(
            "+====================================================================================================================================+")

        if len(lines) == 0:
            print("!!!...NO RECORD EXIST IN SALARY TABLE...!!!")
