# 2. Write a program which accepts one number and prints count of digits in that number. 
# Input: 7521 
# Output:4

def Count_Digits(n):
    return (len(str(n)))

def main():
    n=int(input("Enter Number: "))
    print("Count is: ",Count_Digits(n))



if __name__== "__main__":
    main()        

