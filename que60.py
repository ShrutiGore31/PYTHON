#6. Write a program which accept number from user and check whether that number is positive or negative or zero,
#Input; 11
#Output: Positive Number
#Input: -8
#Output: Negative Number
#Input ; 0
#Output zero

def Check(No):
    if(No > 0):
        print("Positive")

    elif(No < 0):
        print("Negative")

    else:
        print("Zero")

def main():
    x=int(input("Enter Number: "))
    Check(x)

if __name__=="__main__":
    main()                    
