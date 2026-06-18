#Write a program which accepts one number and prints that many numbers starting from 1. 
# Input: 5
# Output: 12345

def PrintNumbers(n):
    for i in range(1, n + 1):                          #while i<=n:              i->1,2,3,4,5,6....    and    n->input by user
        print(i, end=" ")                                #print(i, end=" ")
                                                         #i=i+1

def main():
    x = int(input("Enter a number: "))
    PrintNumbers(x)

if __name__ == "__main__":
    main()
