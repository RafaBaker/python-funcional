from utils import *


def compress(lista):

    if not lista:
        return []
    
    if tail(lista) and head(lista) == head(tail(lista)):
        return [] + compress(tail(lista))

    return [head(lista)] + compress(tail(lista))

def main():
    
    print(compress([1, 2, 2, 2, 3, 4]))
    
    return 0

if __name__=="__main__":
    main()