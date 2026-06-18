#5. Write a program which accepts one number and prints that many numbers in reverse order. 
# Input: 5 
# Output: 5 4 3 2 1

def PrintReverseNumbers(n):
    while n>=1:                                                #you can also this  #for i in range(n,0,-1)                                                    
        print(n,end=" ")                                                          #print(i,end=" ")
        n=n-1
        

def main():
    x=int(input("Enter Number: "))
    PrintReverseNumbers(x)

if __name__=="__main__":
    main()            




         