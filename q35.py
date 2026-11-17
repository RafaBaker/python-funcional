from functools import reduce


def head(lista):
    return lista[0]

def tail(lista):
    return lista[1:]

def init(lista):
    return lista[:-1]

def last(lista):
    return lista[-1]

def pack(lista):
    
    if not lista:
        return []
    
    return reduce(
        lambda x, y: [y] if not x else (
            init(x) + [last(x) + y]
            if head(last(x)) == head(y)
            else x + [y]
        ),
        map(lambda x: [x], lista),
        []
    )
    


def main():
    
    print(pack([1, 2, 3, 3, 4]))
    
    return 0

if __name__=="__main__":
    main()
