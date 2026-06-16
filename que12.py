##5. Write a program which accepts one number and prints all odd numbers till that number.

def Odd(n):
    for i in range(1,n+1,2):
        print(i,end=" ")

def main():
    x=int(input("Enter a number: "))
    Odd(x)

if __name__=="__main__":
    main()            