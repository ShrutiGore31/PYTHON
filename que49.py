# Write a lambda function using reduce() which accepts a list of numbers from user
# and returns the maximum element.


from functools import reduce
Maximum= lambda A,B: A if A>B else B

def main():
    n=int(input("Enter how many numbers you want to enter: "))

    Data=[]

    for i in range(n):
        value= int(input("Enter number: "))
        Data.append(value)

    print("Input List: ",Data )

    Result=reduce(Maximum,Data)
    print("Maximum number is: ",Result)

if __name__=="__main__":
    main()        