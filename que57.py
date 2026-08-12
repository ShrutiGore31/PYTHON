#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.
# input : 11                 output : 16

def Add(A, B):
    return A + B

def main():
    x=int(input("Enter Number : "))
    y=int(input("Enter Number : "))
    Result= Add(x,y)
    print("Addition is: ",Result)

if __name__== "__main__":
    main()    