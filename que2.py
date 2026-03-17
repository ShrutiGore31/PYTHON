#2. Write a program which contains one function ChkGreater () that accepts two numbers and prints the greater number.
#Input: 10 20
#Output: 20 is greater


def ChkGreater(no1,no2):
    if no1>no2:
        print("Greater number is: ",no1)
    else:
        print("Greater number is: ",no2)

def main():
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    ChkGreater(x,y)
   
if __name__=='__main__':
    main()   