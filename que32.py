# Write a lambda function which accepts two numbers and returns maximum number.
# Input: 10  20
# Output: 20

Maximum=lambda A,B: A if A>B else B

def main():
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))

    Result=Maximum(x,y)
    print("Maximum number is: ",Result)

if __name__=="__main__":
    main()
