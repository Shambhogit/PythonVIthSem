class ReadStudent:
    name: str
    roll: int
    department: str
    marks: int

    def getStudent(self):
        self.name = input("Enter Name of Student: ")
        self.roll = int(input("Enter roll number of student: "))
        self.department = input("Enter your Department: ")
        self.marks = int(input("Enter your Marks: "))


class WriteStudent(ReadStudent):
    def printStudent(self):
        print(self.name)
        print(self.roll)
        print(self.department)
        print(self.marks)


stud1 = WriteStudent()
stud1.getStudent()
stud1.printStudent()

