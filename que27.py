#Write a program which accepts one number and checks whether it is perfect number or not.
#Input: 6
#Output: Perfect Number

def CheckPerfect(n):
    SumFactor=0
    for i in range(1,n):
        if n%i==0:
            SumFactor=SumFactor+i

    if SumFactor==n:
        print("Perfect Number")
    else:
        print("Not a perfect number")

def main():
    x=int(int (input("Enter a number: ")))     
    CheckPerfect(x)


if __name__=="__main__":
    main()              