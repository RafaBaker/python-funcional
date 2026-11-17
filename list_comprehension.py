def head(lista):
    return lista[0]

def tail(lista):
    return lista[1:]

def len(palavra):
    if not palavra:
        return 0
    
    return 1 + len(tail(palavra))

# retorna o quadrado dos números pares até n
def quadradosPares(n):

    return [ x*x for x in range (2, n+1) if x % 2 == 0]
    
# retorna as palavras com pelo menos a quantidade de caracteres
def palavrasLongas(palavras, tamanho):
    
    return [ x for x in palavras if len(x) >= tamanho ]

def divisores(n):
    
    return [ x for x in range (1, n+1) if n % x == 0]

def diferencasQuadradas(v, w):
    
    def zip(a, b):
        if not a or not b:
            return []

        return [[head(a)] + [head(b)]] + zip(tail(a), tail(b))
    
    return [ (x-y)*(x-y) for x,y in zip(v, w)]

def paresSoma(n, soma):
    s = [ x for x in range (1, n+1)]
    return [ (x, y) for x in s for y in s if x+y==soma]

def achata(listas):
    
    return [ x for y in listas for x in y]

def main():
    
    print(quadradosPares(8))
    
    print(palavrasLongas(["sol", "casa", "mar", "python"], 5))
    
    print(divisores(12))
    
    print(paresSoma(4, 5))
    
    print(diferencasQuadradas([1, 2, 3], [3, 2, 1]))
    
    print(achata([[1, 2], [], [3], [4, 5]]))
    
    return 0

if __name__=="__main__":
    main()