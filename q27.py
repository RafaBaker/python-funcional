from utils import *
from q26 import splitToken

# retorna o indice que ele aparece
def index(n, lista):

    if not lista:
        return 0

    if n == head(lista):
        return 0

    return 1 + index(n, tail(lista))


def take(lista, index):
    if index < 0:
        return []

    if not lista:
        return []

    return [head(lista)] + take(tail(lista), index-1)

def drop(lista, index):

    if not lista:
        return []

    if index==0:
        return lista

    return drop(tail(lista), index-1)

def joinToken(n, lista):

    if not lista:
        return []

    # if not init(lista):
    #     return []

    return head(lista) + [n] + joinToken(n, tail(lista))

def main():

    lista = [1,2,3,4,2,5,67,8,9,0,3]

    print(index(2, lista))
    print(drop(lista, 1))

    print(splitToken(2, [1,2,3,4,2,5,67,8,9,0,3]))
    print(joinToken(2, splitToken(2, [1,2,3,4,2,5,67,8,9,0,3])))


if __name__ == "__main__":
    main()
