#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
from asyncio import exceptions


# try:
#     n = int(input('enter a number'))
#     if n<=0:
#         raise ValueError("Number must be Positive")
#     else:
#         print(n)
# except ValueError as e:
#     print(e)


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
# class InvalidPasswordError(Exception):
#     pass
# try:
#     p=input('enter a password')
#     if len(p)<8:
#         raise InvalidPasswordError("Password should be 8 characters")
# except Exception as e:
#     print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

class InsuffientBalanceError(Exception):
    pass
try:
    b=int(input('enter balance amound'))
    a=int(input('enter amound to withdraw'))

    if a>b:
        raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
    else:
        print("balance",-(a-b))
except Exception as a:
    print(a)