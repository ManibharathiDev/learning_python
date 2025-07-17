class Employee:
    company = "Suguna Foods"

    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
       return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}")

e1 = Employee(45000,"John Doe",4)
print(e1.get_salary())
print(e1.name)
print(e1.bond)
e1.get_info()