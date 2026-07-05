#15.1  Write a lambda function using map() which accepts a list of numbers (from user)
# and returns a list of squares of each number.
# Input: [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]

Square= lambda No: No*No

def main():
    n=int(input("ENter how many numbers you want to enter: "))

    Data=[]
    for i in range(n):
        value=int(input("Enter a number: "))
        Data.append(value)

    print("Original data is: ",Data)

    Result= list(map(Square,Data))
    print("Data after mapping: ",Result)   

if __name__=="__main__":
    main()