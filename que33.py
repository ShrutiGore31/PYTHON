## Write a lambda function which accepts two numbers and returns minimum number.
# Input: 10  20
# Output: 20

Minimum=lambda A,B: A if A<B else B

def main():
    x=int(input("Enter First number: "))
    y=int(input("Enter Second Number: "))
    Result=Minimum(x,y)
    print("Minimum Number is: ",Result)

if __name__=="__main__":
    main()    