# f=open('k.txt','a')
# f.write(' python')
# f.close()
from dis import print_instructions
from fileinput import filename
from operator import add
from traceback import print_tb

# write aa program to read the content from onr text file and add the conttent into another file
#
# f=open('p.txt','r')
# c=f.read()
# f.close()
# f=open('k.txt','a')
# f.write(" "+c)
# f.close()

# f=open('p.txt','a+')
# print(f.tell())
# f.write(' python')
# f.seek(0)
# print(f.read())
# f.close()
#
# import os
#
# os.remove('p.txt')
# print('removed')
# def sum():
#     n1 = int(input("enter the number"))
#     n2 = int(input("enter the number"))
#     s = n1 + n2
#     print("sum ", s)
# def sub():
#     n1 = int(input("enter the number"))
#     n2 = int(input("enter the number"))
#     su = n1- n2
#     print("sum ", su)
# def mult():
#     n1 = int(input("enter the number"))
#     n2 = int(input("enter the number"))
#     mu = n1 * n2
#     print("sum ", mu)
# def div():
#     n1 = int(input("enter the number"))
#     n2 = int(input("enter the number"))
#     di = n1 / n2
#     print("sum ", di)
#
#
# print('1.add')
# print('2.sub')
# print('3.mult')
# print('4.div')
# ch=int(input('enter your choise :'))
# if ch==1:
#     sum()
# elif ch==2:
#     sub()
# elif ch==3:
#     mult()
# elif ch==4:
#     div()
# else:
#     exit()

def read():
    fn=input('enter file name')
    f=open(fn,'r')
    c=f.read()
    print(c)
    f.close()
def write():
    fn=input('enter file name')
    f=open(fn,'w')
    c=input('eneter your content')
    f.write(c)
    f.close()
def appnd():
    fn = input('enter file name')
    f = open(fn, 'w')
    c = input('eneter your content')
    f.write(c)
    f.close()
def serch():
    fn=input('enter file name')
    f=open(fn,'r')
    c=f.read()
    w=input('enyter the word')
    if w in c:
        print('word found')
    else:
        print("not fournd")
    f.close()
def dlt():
    import os
    fn=input('enter file name')
    os.remove(fn)
    print('file deleted')
while(True):
    print('1.read')
    print('2.write')
    print('3.append')
    print('4.search')
    print('5.delete')
    print('6.exit')
    ch=int(input("enyter choice"))
    if ch==1:
        read()
    elif ch==2:
        write()
    elif ch==3:
        appnd()
    elif ch==4:
        serch()
    elif ch==5:
        dlt()
    else:
        exit
