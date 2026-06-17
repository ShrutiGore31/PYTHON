#write a program which accepts one number and prints sum of digits. Using map
# input=1,2,3,4. 
# output=10

def Sum_Digits(n):
    Digits=map(int,str(n))
    return sum(Digits)

def main():
    x=int(input("Enter Number: "))
    result=Sum_Digits(x)
    print("Sum of Digits is: ",result)

if __name__=="__main__":
    main()    
