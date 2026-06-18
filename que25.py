#Write a program which accepts length and width of rectangle and prints area.

def AreaRectangle(length,width):
    Area=length*width
    return Area

def main():
    l=float(input("Enter length: ")) 
    w=float(input("Enter width: ")) 

    Result=AreaRectangle(l,w)
    print("Area is: ",Result)

if __name__=="__main__":
    main()    