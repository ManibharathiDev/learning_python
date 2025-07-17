# class : class is blueprint or a template 
# Eg Form for an exam that contains name,age,electives and etc.
# Object : Specific instance created from the template (class.).Eg. 
# Form which contains the data for for John Doe

class Employee:
    company = "Suguna Foods"
    
    def get_salary(self):
        print(self) # Self is object of the instance of class
        return 45000
    
e1 = Employee() # An object of class Employee is created here
print(e1.get_salary())  # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)
