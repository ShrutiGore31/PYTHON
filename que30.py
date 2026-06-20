# Write a lambda function which accepts one number and returns square of that number.

Square=lambda No : No*No

def main():
    x=int(input("Enter Number: "))
    Result=Square(x)
    print("Square is: ",Result)

if __name__=="__main__":
    main()    
