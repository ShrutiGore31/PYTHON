#10. Write a program which accept name from user and display length of its name.
#Input : Marvellous
#Output : 10


def length(String):
    return len(String)

def main():
    x=input("Enter String: ")
    Result=length(x)
    print("Length of string is: ",Result)

if __name__=="__main__":
    main()    