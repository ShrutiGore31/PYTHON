# Write a lambda function which accepts three numbers and returns largest number.
# Input: 10  20  15
# Output: 20

Largest= lambda A,B,C: A if (A>B and A>C) else (B if B>C else C)            #Largest = lambda A, B, C : max(A, B, C)

def main():
    x=int(input("Enter 1st number: "))
    y=int(input("Enter 2nd number: "))
    z=int(input("Enter 3rd number: "))

    Result=Largest(x,y,z)
    print("Largest number is: ",Result)

if __name__=="__main__":
    main()    