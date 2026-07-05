# Write a lambda function using filter() which accepts a list of numbers
# and returns a list of odd numbers.
# Input: [11, 10, 15, 20, 22, 27, 30]
# Output: [11, 15, 27]

CheckOdd= lambda No: No%2 !=0

def main():
    Data=[10,11,20,21,30,31,41]
    print("ORiginal Data is: ",Data)

    Result= list(filter(CheckOdd,Data))
    print("Data after filtering is: ",Result)

if __name__=="__main__":
    main()    