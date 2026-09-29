# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
from operator import is_not
# #
# while (True):
#     try:
#         n=int(input('enter the number'))
#         import math
#         print('factorial:',math.factorial(n))
#         break
#     except:
#         print("enter a number as input")




# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# while(True):
#     try:
#
#         print("!.addition")
#         print("2.subtraction")
#         print("3.multiplication")
#         print('4.division')
#         print('5.exit')
#
#         ch=int(input("Enter your choice"))
#         if ch in [1,2,3,4]:
#             n = int(input("Enter number"))
#             m = int(input("Enter a number"))
#             s=n+m
#             d=n-m
#             p=n*m
#             q=n/m
#
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Value Error")
#     except:
#         print("Error")
#     else:
#
#         if ch==1:
#             print("Result",s)
#         elif ch==2:
#             print("Result",d)
#
#         elif ch==3:
#             print("Result",p)
#
#         elif ch==4:
#             print("Result",q)
#
#         else:
#             exit()




# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#     n=input('enter file name to open')
#     f =open(n,'r')
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print('enter correct file name')

#Given a Dictionary
#
# d={"name":"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

try:
    d={"name":"arun","age":23,"place":"ekm"}
    ch=input('enter a key to display')
    print(d[ch])
except KeyError as e:
    # print('enter a valid key')
    print(e)