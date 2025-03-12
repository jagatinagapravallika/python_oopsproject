from employee import *
from utility import *

class EmployeeManager:
    def __init__(self):
        self.employees=[] #list stores the list of employees

    def add_employee(self):
        name=input("enter the name of empoyee ")
        age=input_is_valid("enter the age of employee ")
        salary=input_is_valid("enter the employee salary")
        self.employees.append(Employee(name,age,salary))

    def list_employee(self):
        if len(self.employees)==0:
            print("Employee list is empty")

        else:
            for emp in self.employees:
                print(emp)

    def delete_employees_with_age(self,age_from,age_to):
        self.employees=[emp for emp in self.employees if not (age_from <= emp.age <= age_to)]
        print("employees within the range deleted") 

    def find_employees_with_name(self,name):
        for emp in self.employees:
            if emp.name==name:
                return emp
            
    def update_salary_by_name(self,name,salary):
        emp=self.find_employees_with_name(name)
        if emp is None:
            print("error name")
        else:
            emp.salary=salary
            print(f"updated salary of {name} to {salary}")
