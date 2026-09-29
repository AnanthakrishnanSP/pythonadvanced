# read
import types

f=open('k.txt','r')
# read function returns content as string format
# read lines list format
s=f.read()
print(s)
print(type(s))
f.close()