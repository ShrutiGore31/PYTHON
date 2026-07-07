#Write a lambda function using reduce() which accepts list of numbers and returns count of even numbers

from functools import reduce
CountEven= lambda Count, No : Count + 1 if No%2==0 else Count

def main():
    n=int(input("Enter number of elements: "))
    Data= []

    for i in range(n):
        Value= int(input("enter number: "))
        Data.append(Value)

    print("Input Data: ",Data)

    Result= reduce(CountEven , Data,0)
    print("Count of even Numbers: ",Result)   

if __name__=="__main__":
    main()     