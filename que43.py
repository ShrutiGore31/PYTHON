# Write a lambda function using filter() which accepts a list of numbers (from user)
# and returns a list of even numbers.
# Input: [11, 10, 15, 20, 22, 27, 30]
# Output: [10, 20, 22, 30]

Even= lambda No: No%2==0

def main():
    n=int(input("How many numbers you want to enter: "))

    Data=[]
    for i in range(n):
        value=int(input("Enter a number: "))
        Data.append(value)

    print("Original data: ",Data)

    FData=list(filter(Even,Data))
    print("Data after filtering: ",FData)

if __name__=="__main__":
    main()        