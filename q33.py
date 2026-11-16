from utils import *


def len(string):
    if not string: return 0

    return 1 + len(tail(string))


def inverted(string):
    if not string: return ""

    return last(string) + inverted(init(string))

def isPalindrome(string):
    
    return string == inverted(string)

def main():
    
    print (isPalindrome("ovo"))
    print (isPalindrome("reinier"))
    print (isPalindrome("rever"))
    print (isPalindrome("abacate"))
    print (isPalindrome("Socorram me subi no onibus em Marrocos".lower().replace(" ", "")))
    
    return 0

if __name__=="__main__":
    main()