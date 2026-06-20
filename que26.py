#Write a program which accepts radius of circle and prints area of circle.

import math

def AreaCircle(radius):
    Area=math.pi*radius*radius
    return Area

def main():
    r=float(input("Enter Radius: "))
    Result=AreaCircle(r)
    print("Area of Circle: ",Result)

if __name__=="__main__":
    main()    

