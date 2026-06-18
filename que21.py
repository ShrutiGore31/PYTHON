#2. Write a program which accepts one number and prints its factors.
#Input: 12
#Output: 1 2 3 4 6 12

def Factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=" ")

def main():
    x=int(input("Enter Number: "))
    Factors(x)

if __name__=="__main__":
    main()                


