class Employee:

    name: str
    department: str
    salary: int

    def getEmpInfo(self):
        self.name = input("Enter your name: ")
        self.department = input("Enter Department: ")
        self.salary = int(input("Enter salary: "))

    def printInfo(self):
        print(self.name)
        print(self.department)
        print(self.salary)


emp1 = Employee()
emp1.getEmpInfo()
emp1.printInfo()



