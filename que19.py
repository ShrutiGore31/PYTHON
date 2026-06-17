#5. Write a program which accepts one number and checks whether it is palindrome or not.
#  Input: 121 
# Output: Palindrome


def Palindrome(n):
    Original=n
    rev=0

    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10

    if rev==Original:
        print("It is palindrome")
    else:
        print("it is not a palindrome")        

def main():
    x=int(input("Enter a Number: "))
    Palindrome(x)        

if __name__=="__main__":
    main()    