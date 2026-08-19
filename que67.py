#Write a program which accept one number from user and return its factorial.
#Input: 5
#Output:120

def Factorial(n):
    fact=1
    for i in range(1,n+1):
        fact =fact * i
    return fact
    
def main():
    x=int(input("Enter  number: "))
    result=Factorial(x)
    print("Factorial is: ",result)

if __name__=="__main__":
    main()        