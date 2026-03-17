#3. Write a program which accepts one number and prints square of that number.
#Input: 5
#Output: 25

def Square(n):
    return n*n

def main():
    x=int(input("Enter a number: "))
    result=Square(x)
    print("Square is: ",result)

if __name__=="__main__":
    main()    
    
