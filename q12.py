import utils as u
from q11 import ehPrimo

def f(N):
	return [x for x in range(2, N) if ehPrimo(x)]

# pesquisar o outro jeito de fazer 

def main():
    print(f(15))

if __name__=="__main__":
    main()
