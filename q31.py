from utils import *


def soma(lista):
    if not lista:
        return 0
    
    return soma(tail(lista)) + head(lista)

def pares(v, w):
    
    if not v or not w:
        return []
    
    return [(head(v), head(w))] + pares(tail(v),tail(w))

def escalar(v, w):
    
    return soma([ x*y for x,y in pares(v, w)])

def main():
    
    print(escalar([1, 2], [2, 4]))
    
    return 0

if __name__=="__main__":
    main()