# class parent:
#     def m1(self):
#         print('hi bro parent')
#     def m2(self):
#         print('gd morning parent')
#
# # p=parent()
# # p.m1()
# # p.m2()
#
# class child(parent):
#     def m1(self):
#         print('nthaan bro moda ahno child')
#         super().m1()
#     def m3(self):
#         print('vtl poda child')
# c=child()
# c.m1()
# c.m2()
# c.m3()
from typing import Self
from wsgiref.types import InputStream


# ---------------------------------------------------------------------------------------

# class person():
#     def __init__(self):
#         self.name=input('enter your nAme')
#         self.age=int(input('ENTER ypur age'))
#
#     def show(self):
#         print(self.name,self.age)
# class student(person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input('enter your roll no'))
#         self.course=input('enter your course')
#         self.mark=int(input('enter your mark'))
#     def show(self):
#         super().show()
#         print(self.rollno,self.course,self.mark)
#     def updatemart(self):
#         self.mark=int(input('enter new mark'))
# s=student()
# s.show()
# s.updatemart()

# --------------------------------------------------------------------------------------

# class company():
#     def __init__(self):
#         self.company_name=input('enter company name')
#         self.location=input('enter company location')
#
#     def display_company(self):
#         print(self.company_name)

# class emploe(company):
#     def __init__(self):
#         super().__init__()
#         self.empID=int(input('enter enp id'))
#         self.name=input('enter name')
#         self.salary=int(input('enter salary'))
#     def show(self):
#         super().display_company()
#         print(self.empID,self.name,self.salary)
#     def updatesalary(self):
#         self.salary=1.1*self.salary
#         print('salary increased',self.salary)
#
#
# e=emploe()
# e.show()
# e.updatesalary()

# ------------------------------------------------------------------------------


# class category:
#     def __init__(self):
#         self.category_name=input('enter category')
#     def show_category(self):
#         print(self.category_name)
#
#
# class product(category):
#     def __init__(self):
#         super().__init__()
#         self.produc_name=input('enter prooduct name')
#         self.price=int(input("enter price"))
#         self.quantity=int(input('enter quanitty of producht'))
#     def total_price(self):
#         super().show_category()
#         print(self.price*self.quantity)
#
# p=product()
# p.total_price()

# ------------------------------------------------------------------------------------------------

class hospital:
    def __init__(self):
        self.hos_name=input('enter hospital name')
        self.location=input('hospital lovation')
        self.phone=input  ('enter phone number')
    def display_hospital(self):
        print(self.hos_name)
class department:
    def __init__(self):
        self.depart_name=input('enter dep name')
        self.doctor_name=input('enter doctor name')
    def desplay_dep(self):
        print(self.depart_name,Self.doctor_name)

class patiant(hospital,department):
    def __init__(self):
        hospital.__init__(self)
        department.__init__(self)
        self.patiant_name=input('enter patiant name')
        self.age=int(input('enter age'))
        self.gender=input('enter gender')
        self.admition_date=input('enter admmision date')
        self.bedno=int(input('enter bed no'))
        self.discharge_date=''
    def set_discharge(self):
        self.discharge_date=input('enter discharge date')
    def full_summary(self):
        hospital.display_hospital(self)
        department.desplay_dep(self)
        print('name:',self.patiant_name,'age:',self.age,'gender:',self.gender,'admition date:',self.admition_date,'bed no:',self.bedno,'discharge date:',self.discharge_date)

p=patiant()
p.full_summary()
p.set_discharge()
p.full_summary()