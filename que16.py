#write a program which accepts one number and prints sum of digits. 
# input=1,2,3,4. 
# output=10

def Sum_Digits(n):
    Total=0
    for Digit in str(n):
        Total=Total + int(Digit)
    return Total

def main():
    No=int(input("Enter Number: "))
    Sum=Sum_Digits(No)
    print("Sum is : ",Sum)

if __name__=="__main__":
    main()        