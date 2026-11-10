import utils as u
from q11 import ehPrimo


def proximoPrimo(n):
	if ehPrimo(n+1):
		return n+1
	return proximoPrimo(n+1)

def main():
	
    print(proximoPrimo(3))
    

if __name__=="__main__":
    main()
