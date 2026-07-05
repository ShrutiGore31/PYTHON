# Write a lambda function using filter() which accepts a list of numbers (from user)
# and returns a list of odd numbers.

CheckOdd= lambda No: No % 2 !=0

def main():
    n= int(input("Enter numbers you want to enter: "))

    Data=[]

    for i in range(n):
        value= int(input("Enter Number: "))
        Data.append(value)

    print("Original list: ",Data)

    FData=list(filter(CheckOdd,Data))
    print("Odd numbers list is: ",FData)

if __name__=="__main__":
    main()        