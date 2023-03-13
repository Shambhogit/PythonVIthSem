from AddEmployee import AddEmployee
from DeleteEmp import DeleteEmp
from DisplayEmp import DisplayEmp
from Payment import Payment
from SalaryTable import SalaryTable
from SearchEmployee import SearchEmployee
from UpdateInformation import UpdateInformation


class Main:
    __userId = "Shambho123"
    __password = "shambho"

    def menu_function(self) -> None:
        while True:
            print("===========================================================================================")
            print('''Choose From following Menu
               1.ADD EMPLOYEE
               2.DELETE EMPLOYEE
               3.UPDATE INFORMATION
               4.SEARCH EMPLOYEE
               5.PAY SALARY
               6.DISPLAY EMPLOYEE TABLE
               7.DISPLAY SALARY TABLE
               8.LOG-OUT ADMIN''')
            print("===========================================================================================")
            try:
                choise = int(input("Enter your choice...\n"))
                print("===========================================================================================")
                match choise:
                    case 8:
                        print("YOUR LOGGED OUT NOW \nTHANKS FOR USING SYSTEM")
                        print(
                            "===========================================================================================")
                        break
                    case 1:
                        AddEmployee.add_employee(self)
                    case 2:
                        DeleteEmp.delete_employee(self)
                    case 3:
                        UpdateInformation.update_information(self)
                    case 4:
                        SearchEmployee.search_employee(self)
                    case 5:
                        Payment.payment(self)
                    case 6:
                        DisplayEmp.display_emp(self)
                    case 7:
                        SalaryTable.print_salary_table(self)

            except:
                print("WRONG INPUT....!!!")

    def logIn_function(self) -> None:
        count = 0
        while count < 5:
            count = count + 1
            print("===========================================================================================")
            userId = input("Enter your User ID : ")
            password = input("Enter your Password : ")
            print("===========================================================================================")
            if userId.__eq__(self.__userId) and password.__eq__(self.__password):
                print("Logged in to the system...!")
                Main.menu_function(self)
                break
            else:
                print("Wrong UserId or Password\n")
                print("===========================================================================================")

        if (count == 5):
            print("you Entered Wrong password five time")


a = Main()
a.logIn_function()
