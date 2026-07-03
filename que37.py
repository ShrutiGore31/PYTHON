# Write a lambda function which accepts two numbers and returns addition.
# Input: 10  20
# Output: 30

Addition= lambda A,B: A+B

def main():
    x=int(input("Enter First number: "))
    y=int(input("Enter Second Number: "))
    Result=Addition(x,y)
    print("Addition is: ",Result)

if __name__=="__main__":
    main()    


