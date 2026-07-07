# Write a lambda function using filter() which accepts list of strings from user
# and returns a list of strings having length greater than 5.

CheckLength= lambda S : len(S) > 5

def main():
    
    n = int(input("Enter how many strings you want to enter: "))
    Data = []

    for i in range(n):
        Strings = input("Enter a string: ")
        Data.append(Strings)

    print("Input Data is: ",Strings)

    Result = list(filter( CheckLength, Data))
    print("Data which is having more than 5 len is: ",Result)

if __name__=="__main__":
    main()        
