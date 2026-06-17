#4. Write a program which accepts one number and prints reverse of that number.
#  Input: 123
#  Output: 321

def ReverseNumber(n):                     #defined a function name as Reverse number and n is number given by user
    rev=0                                 #this variable will store reverse number. we statrt with 0
    while n>0:                            # used while loop.it runs until n becomes 0
        digit= n%10                       #using modulus we extract the last digit of number. ex-> 123%10=3
        rev=rev *10 +digit                #it builds the reverse. ex.rev = 0 → 0*10 + 3 = 3,rev = 3 → 3*10 + 2 = 32,rev = 32 → 32*10 + 1 = 321
        n=n//10                           #removes last digit so number slowly becomes 0 and loop stops
    return rev                            #it return revised number to the function

def main():                               #main function starts.which controls program flow
    x=int(input("Enter Number: "))        #takes input from user and convert it to integer
    No=ReverseNumber(x)                   #calls the function
    print("Reversed number is: ",No)      #prints the revised number

if __name__=="__main__":                  #ensures that program execution starts from main
    main()                                #main starts
    