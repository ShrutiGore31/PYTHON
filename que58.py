#  write a program which display 5 times marvellous on screen
# output: marvellous
#         marvellous
#         marvellous
#         marvellous
#         marvellous


def Display(n):
    for i in range(n):
        print("Marvellous")
       
def main():
    x=int(input("Enter how many times you want to enter it: "))
    Result=Display(x)


if __name__=="__main__":
    main()            
