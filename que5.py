#5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
#Input: 15
#Output: Divisible by 3 and 5

def ChkDivisiblity(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Number is divided by 3 and 5")
    else:
        print("not divided by 3 and 5")  

def main():
    x=int(input("Enter a number: "))
    ChkDivisiblity(x)

if __name__=="__main__":
    main()    
              
