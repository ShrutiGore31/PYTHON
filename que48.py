# Write a lambda function using reduce() which accepts a list of numbers
# and returns the maximum element.


from functools import reduce
Maximum= lambda A,B: A if A>B else B

def main():
    Data= [11,21,51,101,111]

    print("Data in list: ",Data)

    Result= reduce(Maximum,Data)
    print("Maximum is: ",Result)

if __name__=="__main__":
    main()    