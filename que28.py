#Write a program which accepts one number and prints its binary equivalent.
#Input: 5
#Output: 101

def BinaryEquivalent(n):
    binary=""

    while(n>0):
        remainder=n%2
        binary=str(remainder) + binary
        n=n//2

    print("Binary equvalent: ",binary)

def main():
    x=int(input("Enter Number: "))
    BinaryEquivalent(x)

if __name__=="__main__":
    main()            