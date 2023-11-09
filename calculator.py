#Design a simple calculator with basic arithmetic operations.

#taking 2 input values from user
print("Enter two numbers:")
num1 = float(input())
num2 = float(input())

#choose an option to perfom an arithmatic operation
print('choose one option:')
print('addtion=1')
print('substraction=2')
print('multiplication=3')
print('division=4')

#taking input choice to perform an operation
choice=int(input())

if(choice==1):
    print(num1,'+',num2,'=',num1+num2)

#substraction using format specifier
elif(choice==2):
    print(num1,'-',num2,'=',num1-num2)

#multiplication operation
elif(choice==3):
    print(num1,'*',num2,'=',num1*num2)

elif(choice==4):
#division using try except 
    try:
        x = num1/num2
        print(x)
    except ZeroDivisionError:
        print('Can not divide by zero')
else:
    print('invalid operator')
