#Write a program which accept one number and display below pattern.
#Input:5
#Output:
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#*   *   *   *   *
#(5 rows and 5 columns of stars)

def Pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()        

def main():
    x=int(input("Enter Number: "))
    Pattern(x)

if __name__=="__main__":
    main()                