#3. Write a program which accepts one number and prints factorial of that number.
#Input: 5
#Output: 120

def Factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

def main():
    x=int(input("Enter number: "))
    ans=Factorial(x)
    print("Factorial is: ",ans)

if __name__=="__main__":
    main()        