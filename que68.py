#Write a program which accepts one number from the user and returns the addition (sum) of its factors.
#Example
#Input:6
#Factors of 6 are: 1, 2, 3, 6
#Output:
# Sum of factors = 12

def SumFactors(n):
    sum=0

    for i in range(1, n+1):
        if(n%i==0):
            sum= sum + i
    return sum

def main():
    x=int(input("Enter number: "))
    result=SumFactors(x)
    print("Sum is: ",result)

if __name__=="__main__":
    main()            