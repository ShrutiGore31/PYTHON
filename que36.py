# Write a lambda function which accepts one number and returns True if divisible by 5.
# Input: 25
# Output: True

CheckDivisible=lambda No: True if No%5==0 else False

def main():
    x=int(input("Enter Number: "))
    Result=CheckDivisible(x)
    print("Result is: ",Result)

if __name__=="__main__":
    main()    