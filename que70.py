#6. Write a program which accept one number and display below pattern.
#Input : 5
#output: 
#   *   *   *   *   *
#   *   *   *   *
#   *   *   *
#   *   *
#   *

def DisplayPattern(No):

    for i in range(No, 0, -1):
        for j in range(1, i+1):
            print("*", end="\t")

        print()


def main():

    Value = int(input("Enter number: "))

    DisplayPattern(Value)


if __name__ == "__main__":
    main()