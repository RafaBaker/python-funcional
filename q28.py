from q10 import f
from utils import *


def take(lista, n):
    
    if not lista:
        return []

    if n < 0:
        return []
    
    return [head(lista)] + take(tail(lista), n-1)

def drop(lista, n):
    
    if not lista:
        return []
    
    if n<0:
        return lista
    
    return drop(tail(lista), n-1)

def splitHalf(lista):
    metade = f(lista) // 2
    return [take(lista, metade)] + [drop(lista, metade)]

def main():

    lista = [1, 2, 3, 4, 5]
    
    print(take(lista, 0))
    print(drop(lista, 0))
    
    print(splitHalf(lista))


if __name__ == "__main__":
    main()
  