from q24 import primes


def conta_freq(n, lista):
    return len(list(filter(lambda x: x == n, lista)))


def agrupa_fatores(lista):
    if not lista:
        return []

    return [(lista[0], conta_freq(lista[0], lista))] + agrupa_fatores(
        list(filter(lambda x: x != lista[0], lista))
    )


def primeFactors(n):
    return agrupa_fatores(primes(n))


def main():
    print(primeFactors(8))
    print(primeFactors(42))


if __name__ == "__main__":
    main()
