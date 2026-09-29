# # #write a program to read a text file and displays the number of lines in a file
from queue import PriorityQueue

# f=open('k.txt','r')
# s=f.readlines()
# print(s)
# print(len(s))
# f.close()

# # #write a program to display the number of words in a file

# f=open('k.txt','r')
# s=f.read()
# print(len(s.split()))


# # #write a program to update the second line in a file

# f=open('k.txt','r')
# s=f.readlines()
# print(s)
# s[1]='hellow\n'
# f.close()

# f=open('k.txt','w')
# f.writelines(s)
# f.close()


# # #write a program to display the last 5 lines in a file

# f=open('k.txt','r')
# s=f.readlines()
# print(s[-2:])
# f.close()

# #program to search a particular word in a file

# f=open('k.txt','r')
# s=f.read()
# if 'hi' in s:
#     print(s)
# else:
#     print('not found')
# f.close()

# #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# s=f.read()
# l=0
# d=0
# sp=0
# for i in s:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         sp+=1
# print(l,d,sp)
# f.close()




#reverse the lines in a file
# f=open('k.txt','r')
# s=f.read()
# print(s[::-1])



# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
f=open('STUDENT','r')
s=f.read()
print(s)
# # Find the students who did not pass.

# # Write their names to a new file named failed_students.txt, one name per line.
# #