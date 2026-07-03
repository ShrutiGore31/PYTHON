# Write a lambda function which accepts two numbers and returns multiplication.
# Input: 5  4
# Output: 20

Multiplication= lambda A,B: A*B

def main():
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    Result=Multiplication(x,y)
    print("Multiplication is: ",Result)

if __name__=="__main__":
    main()    