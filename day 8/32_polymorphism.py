class FullTimeEmployee:
    def compute(self,days):
        salary = 10*days
        print(f"Salary: {salary}")
        
class PartTimeEmployee:
    def compute(self,days):
        salary = 10*days
        print(f"Salary: {salary}")
        
def SalaryCalc(employee, days):
    employee.compute(days)
        
fte = FullTimeEmployee()
pte = PartTimeEmployee()

SalaryCalc(fte, 250)
SalaryCalc(pte, 250)
