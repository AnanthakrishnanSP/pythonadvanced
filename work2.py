# Write a menu-driven Python program using a class Student
#     to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
class student:
    def __init__(self):
        self.rollno = int(input('enter roll no: '))
        self.name = input('enter name: ')
        self.mark = int(input('enter your mark: '))


st = []

while True:
    print('1. add student')
    print('2. update mark')
    print('3. all student details')
    print('4. search by roll number')
    print('5. delete student')
    print('6. exit')

    ch = int(input("Enter your choice: "))

    if ch == 1:
        s = student()
        st.append(s)
        print('added successfully')

    elif ch == 2:
        roll = int(input('enter roll number: '))

        for i in st:
            if i.rollno == roll:
                i.mark = int(input('enter new mark: '))
                print('mark updated')
                break
        else:
            print('student not found')

    elif ch == 3:
        if len(st) == 0:
            print('no students found')
        else:
            for i in st:
                print('Roll No:', i.rollno)
                print('Name:', i.name)
                print('Mark:', i.mark)
                print('----------------')

    elif ch == 4:
        roll = int(input('enter roll number: '))

        for i in st:
            if i.rollno == roll:
                print('Roll No:', i.rollno)
                print('Name:', i.name)
                print('Mark:', i.mark)
                break
        else:
            print('student not found')

    elif ch == 5:
        roll = int(input('enter roll number: '))

        for i in st:
            if i.rollno == roll:
                st.remove(i)
                print('student deleted')
                break
        else:
            print('student not found')

    elif ch == 6:
        break

    else:
        print('invalid choice')