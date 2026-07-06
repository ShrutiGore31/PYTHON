# Write a lambda function using reduce() which accepts a list of numbers from user
# and returns the minimum element.


from functools import reduce
Minimum= lambda A,B: A if A<B else B

def main():
    n=int(input("Enter how many numbers you want to enter: "))
    Data=[]

    for i in range(n):
        Value=int(input("Enter number: "))
        Data.append(Value)

    print("Input list: ",Data)

    Result=reduce(Minimum,Data)
    print("Minimum is: ",Result)

if __name__=="__main__":
    main()       
