'''
Write a program which accept number from user and return addition of digits in that number.

Input :
5187934

Output :
37

Explanation:

5 + 1 + 8 + 7 + 9 + 3 + 4 = 37

'''


def AdditionDigits(No):
    Total=0
    for i in str(No):
        Total = Total + int(i)
    return Total

def main():
    value= int (input("Enter number: "))
    Result=AdditionDigits(value)
    print("Addition is: ",Result)


if __name__=="__main__":
    main()        