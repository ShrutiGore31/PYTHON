# write a program which display 10 to 1 screen
# output : 10 9 8 7 6 5 4 3 2 1

def Display(n):
 
    while n>=1:
        print(n,end=" ")
        n=n-1

def main():
    x= int(input("Enter Number: "))
    Display(x)

if __name__=="__main__":
    main()
