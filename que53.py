# Write a lambda function using reduce() which accepts list of numbers
# and returns product of all elements

from functools import reduce
Multiply= lambda A,B : A*B

def main():
    n=int(input("Enter how many numbers you want to enter: "))
    Data= []

    for i in range(n):
        Value = int(input("Enter Number: "))
        Data.append(Value)

    print("Input Data: ",Data)

    Result= reduce(Multiply,Data)
    print("Final Result: ",Result)

if __name__=="__main__":
    main()        