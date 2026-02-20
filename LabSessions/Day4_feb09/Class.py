class Employee:
    emp_id = 22222
    emp_name = "varun"
    emp_dept = "cs"

    def employee_details(self):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_dept)


b = Employee()
b.employee_details()