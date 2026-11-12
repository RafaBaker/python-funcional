import utils as u

# retorna o indice que ele aparece
def index(n, lista):

    if not lista:
        return 0

    if n == u.head(lista):
        return 0

    return 1 + index(n, u.tail(lista))


def take(lista, index):
    if index < 0:
        return []

    if not lista:
        return []

    return [u.head(lista)] + take(u.tail(lista), index-1)

def drop(lista, index):

    if not lista:
        return []

    if index==0:
        return lista

    return drop(u.tail(lista), index-1)

def splitToken(n, lista):

    if not lista:
        return []

    i = index(n, lista)
    return [take(lista, i-1)] + splitToken(n, drop(lista, i+1))

def main():

    lista = [1,2,3,4,2,5,67,8,9,0,3]

    print(index(2, lista))
    print(drop(lista, 1))

    print(splitToken(2, [1,2,3,4,2,5,67,8,9,0,3]))


if __name__ == "__main__":
    main()
