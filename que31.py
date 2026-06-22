# Write a lambda function which accepts one number and returns cube of that number.
# Input: 3
# Output: 27

Cube= lambda No: No*No*No

def main():
    x= int(input("Enter a number: "))
    Result=Cube(x)
    print("Cube is: ",Result)

if __name__=="__main__":
    main()    