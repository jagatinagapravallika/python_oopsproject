from employeemanager import *

class FrontendManager:
    def __init__(self):
        self.EmployeeManager=EmployeeManager()

    def print_menu(self):
        print("\nOptions to be select")
        messages=[
            '1.Add a new employee',
            '2.List of employees',
            '3.Delete by age range',
            '4.Update salary given a name',
            '5. End the program'
        ]
        print('\n'.join(messages))
        msg=f'enter the choice of operation (1 to {len(messages)})'
        return input_is_valid(msg,1,len(messages))
    
    def run(self):
        while True:
            choice=self.print_menu()

            if choice == 1:
                self.EmployeeManager.add_employee()

            elif choice == 2:
                self.EmployeeManager.list_employee()

            elif choice == 3:
                age_from=input_is_valid("enter the age")
                age_to=input_is_valid("enter the age")
                self.EmployeeManager.delete_employees_with_age(age_from,age_to)

            elif choice ==4:
                name=input("enter the name of employee")
                salary=input_is_valid("employee salary ")
                self.EmployeeManager.update_salary_by_name(name,salary)

            else:
                print("exit program")
                break
