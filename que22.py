#Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Operations(a,b):
    print("Addition is: ",a+b)
    print("Subtraction is: ",a-b)
    print("Multiplication is: ",a*b)
    print("Division is: ",a/b)

def main():
    x=int(input("Enter First Number : "))    
    y=int(input("Enter Second Number : "))  
    Operations(x,y)

if __name__=="__main__":
    main()    