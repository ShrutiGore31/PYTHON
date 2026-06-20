#Write a program which accepts marks and displays grade.
#Condition:
#>=75 → Distinction
#>=60 → First Class
#>=50 → Second Class
#<50  → Fail

def Display(marks):
    if(marks>=75):
        print("Distinction")
    elif(marks>=60):
        print("First Class")
    elif(marks>=50):
        print("Second Class")
    else:
        print("Fail")

def main():
    x=int(input("Enter Marks: "))
    Display(x)


if __name__=="__main__":
    main()                        
