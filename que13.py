#1. Prime Number

def ChkPrime(n):
    if n<=1:
        print("Not a prime number")
        return
    
    Count=0
    for i in range(1,n+1):
        if n%i==0:
            Count=Count+1

    if Count==2:        
        print("Prime number")
    else:
        print("Not a prime number")

def main():
    x=int(input("Enter Number: "))
    ChkPrime(x)

if __name__=="__main__":
    main()            