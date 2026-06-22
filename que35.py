##Write a lambda function which accepts one number and returns True if number is odd otherwise False

CheckOdd= lambda No: True if No%2 !=0 else False

def main():
    x=int(input("Enter a number: "))
    Result=CheckOdd(x)
    print("Result is : ",Result)

if __name__=="__main__":
    main()    