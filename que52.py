# Write a lambda function using filter() which accepts list of numbers from user
# and returns a list of numbers divisible by both 3 & 5

CheckDivisible = lambda No : No %3==0 and No %5==0

def main():
    n= int(input( "Enter how many numbers you want to enter: "))
    Data= []

    for i in range(n):
        Value=int(input(" Enter Number: "))
        Data.append(Value)

    print("Input Data: ",Data)

    Result= list(filter(CheckDivisible,Data))
    print("Numbers which are divisible by 3 & 5 are: ",Result)

if __name__== "__main__":
    main()        