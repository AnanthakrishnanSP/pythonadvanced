# class Person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person('arun',23)
# p2=Person('arum',34)
# p1.show()
# p2.show()
from unittest import enterModuleContext


# class Person:
#     def __init__(self):
#         self.name=input('enter name')
#         self.age=int(input('enter age'))
#
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person()
# p2=Person()
# p1.show()
# p2.show()

# define a class named emploe with atributes emp id,name,age,place,


# class employe:
#     def __init__(self):
#         self.emp_ID=int(input('enter id'))
#         self.name=input('enter name')
#         self.age=int(input('enter id'))
#         self.place=input('enter place')
#         self.slary=int(input('enter slary'))
#         self.designation=input('enter designation')
#
#     def getsalary(self):
#         print(self.slary)
#     def getpersonaldetails(self):
#         print(self.name,self.age)
# e=employe()
# e.getsalary()
# e.getpersonaldetails()

# define a class named student with attributes roll no .name ,mark1,mark2,mark3 and m
# mrthods ddisplay() to display roll no and toyal mark

# class student:
#     def __init__(self):
#         self.rollNo=int(input('enter roll no:'))
#         self.name=input('enter name:')
#         self.mark1=int(input('enter mark1:'))
#         self.mark2=int(input('enter mark2:'))
#         self.mark3=int(input('enter mark3:'))
#
#     def display(self):
#         print('roll NO:',self.rollNo,'total mark:',self.mark1+self.mark3+self.mark2)
#
# s1=student()
# s1.display()
#
# s2=student()
# s2.display()

class book:
    def __init__(self):
        self.title=input('enter the titile')
        self.author=input('enter the auth')
        self.price=int(input('enter the price'))
        self.pages=int(input('enter the pages'))
        self.lang=input('enter the lang')

    def gettitle(self):
        print(self.title)
    def getauth(self):
        print(self.author)
    def getprice(self):
        print(self.price)

    def settitle(self):
        self.title=input('enter new title')
        self.gettitle()
    def setauthor(self):
        self.author=input('enter new auth')
        self.getauth()
    def setprice(self):
        self.price=input('enter new price')
        self.getprice()

b=book()
b.gettitle()
b.settitle()