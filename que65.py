#Create one module named as Arithmetic which contains 4 functions as
# Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accept two parameters as number and perform the operation.
#  Write one python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic
def Operation(a,b):
    print("Addition is: ",Arithmetic.Addition(a , b))
    print("Subtraction is: ",Arithmetic.Subtraction( a , b))
    print("Multiplication is: ", Arithmetic.Multiplication(a , b))
    print("Division is: ",Arithmetic.Division(a , b))


def main():
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    Operation(x,y)

if __name__=="__main__":
    main()    
        
