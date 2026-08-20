'''
18.1. Write a program which accept N numbers from user and store it into List.
Return addition of all elements from that List.

Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
'''

def SumList(No):
    TOtal =0
    for i in No:
        TOtal= TOtal + i
    return TOtal

def main():
    value=int(input("Enter Number of elements: "))

    Data = []

    for i in range(value):
        Number=int (input("Enter number: "))
        Data.append(Number)

    print("List is: ",Data)


    Result=SumList(Data)

    print("Addition of elements is: ",Result)


if __name__=="__main__":
    main()        
