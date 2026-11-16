from q24 import primes
from utils import *


def fatores(n):
    
    return [x for x in range(1, n) if n % x == 0]
    

def soma(lista):
    if not lista:
        return 0
    return head(lista) + soma(tail(lista))

def perfects(n):
    numeros = [x for x in range(2, n+1)]
    
    # somas = [ soma(primes(x)) for x in numeros]
    # print(somas)
    
    # fat = [ fatores(x) for x in numeros]
    # print(fat)
    
    perfects = [ x for x in numeros if soma(fatores(x))==x ]
    # print(perfects)
    
    return perfects

def main():

    print(soma(fatores(6)))
    print(perfects(500))

if __name__ == "__main__":
    main() 