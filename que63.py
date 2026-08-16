#9. Write a program which display first 10 even numbers on screen.
# Output :2 4 6 8 10 12 14 16 18 20

# Program to display first 10 even numbers

def DisplayEven():
    for i in range(1, 11):                                            #for i in range(1,21,2)
        print(i * 2, end=" ")                                         #print (i)

def main():
    DisplayEven()

if __name__ == "__main__":
    main()