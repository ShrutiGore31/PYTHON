#B. Write a program which accept number from user and print that number of "*" on screen.


def Star(No):
    for i in range(No):                                                # print("*" * No) also write it as like this
        print("*", end= " ")

def main():
    x=int(input("Enter number: "))
    Star(x)
    

if __name__=="__main__":
    main()            