#4. Write a program which accepts one number and prints all even numbers till that number.
#Input: 10
#Output: 2 4 6 8 10

def Even(n):
    for i in range(1,n+1):
        if (i%2==0):
            print(i,end=" ")

def main():
    x=int(input("Enter a number: "))
    Even(x)

if __name__=="__main__":
    main()