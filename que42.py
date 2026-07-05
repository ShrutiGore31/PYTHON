#Write a lambda function using filter () which accepts a list of numbers and returns a list of even numbers.

Even= lambda No : No%2==0

def main():
    Data=[10,11,20,21,50,51]
    print("Provided data is: ",Data)

    FData=list(filter(Even,Data))
    print("Data after filter: ",FData)

if __name__=="__main__":
    main()   