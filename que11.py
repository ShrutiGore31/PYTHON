#5. Write a program which accepts one number and prints all odd numbers till that number.

def odd(n):
    for i in range(1,n+1):
        if i%2!=0:
            print(i,end=" ")

def main():
    x=int(input("Enter a number: "))
    odd(x)

if __name__=="__main__":
    main()                


