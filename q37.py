from functools import reduce

from q36 import *


def decode(data):

    return reduce(lambda x, y: x+y, list(map(aux, data)))

def aux(tupla):
    
    return head(tupla) * head(tail(tupla))

def main():
    
    print(aux((4, 'a')))
    
    print(encode("aaaabccaadeeee"))
    print(decode(encode("aaaabccaadeeee")))
    
    
    return 0

if __name__=="__main__":
    main()