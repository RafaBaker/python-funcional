import utils as u
from q24 import primes


def conta_freq(n, lista):
    return len(list(filter(lambda x: x == n, lista)))


def agrupa_fatores(lista):
    if not lista:
        return []

    return [(u.head(lista), conta_freq(u.head(lista), lista))] + agrupa_fatores(
        list(filter(lambda x: x != u.head(lista), lista))
    )


def primeFactors(n):
    return agrupa_fatores(primes(n))


def main():
    print(primeFactors(8))
    print(primeFactors(42))


if __name__ == "__main__":
    main()
