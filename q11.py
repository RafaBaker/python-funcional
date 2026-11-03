import utils as u

def ehPrimo(n):
    return aux(n, n-1)

def aux(n, a):
    if (a <= 1):
        return True
    if (n % a == 0):
        return False
    return aux(n, a-1)

def main():
    print(ehPrimo(17))

if __name__=="__main__":
    main()
