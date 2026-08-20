'''
Write a program which accept number from user and return number of digits in that number.

Input :
5187934

Output :
7

Explanation:
The number 5187934 contains 7 digits, so the output is 7.

'''


def CountDigit(No):
    Count=0

    while(No>0):
        Count= Count + 1
        No= No//10
    return Count

def main():
    value= int(input("Enter Number: "))
    Result= CountDigit(value)
    print("Count is: ",Result)    

if __name__=="__main__":
    main()    