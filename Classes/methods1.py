class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    @staticmethod
    def welmessage():
        print("this is welcome message")

employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welmessage()
