#15.1  Write a lambda function using map() which accepts a list of numbers
# and returns a list of squares of each number.
# Input: [1, 2, 3, 4, 5]
# Output: [1, 4, 9, 16, 25]

Square= lambda No: No*No

def main():
    Data=[11,21,51,101,111]
    print("The Data is: ",Data)

    Result=list(map(Square,Data))
    print("Square is: ",Result)

if __name__=="__main__":
    main()    