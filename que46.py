# Write a lambda function using reduce() which accepts a list of numbers
# and returns the addition of all elements.

from functools import reduce

Addition= lambda A,B: A+B

def main():
    Data=[11,21,51,101,111]

    print("Original Data: ",Data)

    Result= reduce(Addition,Data)
    print("Final output: ",Result)

if __name__=="__main__":
    main()    