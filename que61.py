#7. Write a program which contains one function that accept one number from user 
# and returns true if number is divisible by 5 otherwise retum false.
#Input : 8
#Output False
#Input : 25
#Output - True


def CheckDivisibility(No):
    if No % 5==0:
        return True
    else:
        return False
    
def main():
    x=int(input("Enter Number: "))
    Result=CheckDivisibility(x)
    print(Result)

if __name__=="__main__":
    main()