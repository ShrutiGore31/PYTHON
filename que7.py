#2. Write a program which accepts one number and prints sum of first N natural numbers.
#Input: 5
#Output: 15


def SumNatural(n):
    Total=0
    for i in range(1,n+1):
        Total=Total+i
    return Total

def main():
    x=int(input("Enter a number: "))
    Result=SumNatural(x)
    print("Sum is: ",Result)

if __name__=="__main__":
    main()    
        
