#2. Write a program which accepts one number and prints count of digits in that number.
#  Input: 7521
#  Output:4


def CountDigits(n):
    Count=0
    while n>0:
        Count=Count+1
        n=n//10
    return Count

def main():
    x=int(input("Enter number: "))    
    Result=CountDigits(x)
    print("Count of digits: ",Result)

if __name__=="__main__": 
    main()   
