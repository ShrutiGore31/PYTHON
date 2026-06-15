#4. Write a program which accepts one number and prints all even numbers till that number.
#Input: 10
#Output: 2 4 6 8 10

def Even(n):
    for i in range(2,n+1,2):
        print(i,end=" ")

def main():
    x=int(input("Enter a Number: "))    
    Even(x)    

if __name__=="__main__":
    main()    
