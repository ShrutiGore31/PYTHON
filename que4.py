#Write a program which accepts one number and prints cube of that number.

def Cube(n):
    return n*n*n

def main():
    x=int (input("Enter a number: "))
    Result=Cube(x)
    print("Cube is: ",Result)

if __name__ =="__main__":
    main()   