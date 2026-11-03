import utils as u
from factorial import factorial


def f(n):
    if n==0:
        return 1
    return 1/factorial(n) + f(n-1)

def main():
    print(f(11))

if __name__=="__main__":
    main()
