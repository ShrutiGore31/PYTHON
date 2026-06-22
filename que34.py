#Write a lambda function which accepts one number and returns True if number is even otherwise False.

CheckEven= lambda No: True if No%2==0 else False                    #ChkEven=lambda No: No%2==0

def main():
    x=int(input("Enter a Number: "))
    Result=CheckEven(x)
    print("Result is: ",Result)

if __name__=="__main__":
    main()    