# from abc import ABC,abstractmethod
#
# class shapes(ABC):
#     @abstractmethod
#     def area():
#         pass
#     @abstractmethod
#     def peremeter():
#         pass
#
# class rectangle(shapes):
#     def __init__(self):
#         self.length=int(input('enter the length'))
#         self.breadth=int(input('enter the breadth'))
#
#     def area(self):
#         print('area',self.length*self.breadth)
#     def peremeter(self):
#         print('peremter',2*(self.length+self.breadth))
#
# r=rectangle()
# r.area()
# r.peremeter()

# ----------------------------------------------------------------
# e an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.


from abc import ABC,abstractmethod
class employe(ABC):
    def __init__(self):
        self.empID=int(input('enter empID'))
        self.age=int(input('enter age'))
        self.name=input('enter name')
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(employe):
    def __init__(self):
        super().__init__()
        self.salary=int(input('enter the full time salary'))
    def calculate_salary(self):
        print('salary',self.salary())
class PartTimeEmployee(employe):
    def __init__(self):
        super().__init__()
        self.hours=int(input('enter the hours you have worked'))
        self.pay=int(input('enter your hourly pay'))
    def calculate_salary(self):
        print('salary',self.hours*self.pay)

e=FullTimeEmployee()
e.calculate_salary()