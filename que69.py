#5. Write a program which accept one number for user and check whether number is prime or not.
#Input : 5
#Output : It is Prime Number

def CheckPrime(No):
    i=0
    flag=True

    if(No<=1):
        flag= False

    for i in range(2,No):
        if No % i == 0:
            flag = False
            break
    return flag

def main():
    Value= int(input("Enter Number: "))
    Result= CheckPrime(Value)

    if(Result==True):
        print("It is prime number")

    else:
        print("Not a prime number")


if __name__=="__main__":
    main()           