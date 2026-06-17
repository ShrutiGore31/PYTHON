#1. Write a program which accepts one character and checks whether it is vowel or consonant.
#Input: a
#Output: Vowel

def ChlVowel(N):
    if N in('a','e','i','o','u','A','E','I','O','U'):
        print("Vowel") 
    else:
        print("Consonant")
def main():
    x=input("Enter character: ")
    ChlVowel(x)


if __name__=="__main__":
    main()            



#you can also write it like this->

#def CheckVowel(ch):
#    vowels = {'a','e','i','o','u'}
#    if ch.lower() in vowels:
#        print("Vowel")
#    else:
#        print("Consonant")
#def main():
   