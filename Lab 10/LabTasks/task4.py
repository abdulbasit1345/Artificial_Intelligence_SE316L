class Employee:
    employee_count = 0

    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def displayCount(cls):
        print(f"Total number of employees: {cls.employee_count}")


    def displayEmployee(self):
        print(f"Employee Name: {self.empName}, Salary: {self.salary}")


emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

Employee.displayCount()

emp1.displayEmployee()
emp2.displayEmployee()
