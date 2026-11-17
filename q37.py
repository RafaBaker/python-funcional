from functools import reduce

from q36 import *


def decode(data):

    return reduce(
        lambda x, y: x+y,
        list(map(
            lambda x:
                head(x) * head(tail(x)),
                data)))


def main():
    
    
    print(encode("aaaabccaadeeee"))
    print(decode(encode("aaaabccaadeeee")))
    
    
    return 0

if __name__=="__main__":
    main()