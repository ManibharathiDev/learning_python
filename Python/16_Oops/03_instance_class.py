class Employee:
    company = "Suguna Foods" # This is a class attribute

    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
    
    def get_salary(self):
       return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}")

e1 = Employee(45000,"Sainithran",5,"Tesla")
print(e1.company) # will always print instance attribute whenver present
print(Employee.company) # This will always print instance attribute whenver present

# Object introspection

print(dir(e1)) # Get the all attributes and methods