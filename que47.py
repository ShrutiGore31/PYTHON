# Write a lambda function using reduce() which accepts a list of numbers from user
# and returns the addition of all elements.


from functools import reduce
Addition= lambda A,B: A+B

def main():
    n=int(input("Enter how many numbers you want to enter: "))

    Data=[]

    for i in range(n):
        value=int(input("Enter number: "))
        Data.append(value)

    print("data in the list: ",Data)

    Result= reduce(Addition,Data)
    print("Final output: ",Result)

if __name__=="__main__":
    main()        