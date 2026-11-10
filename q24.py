import utils as u
from q11 import ehPrimo
from q12 import f 

def alguem_divide(n, primos):
	
	print("primos: ")
	print(primos)
	
	
	
	if not primos: 
		return 2
	
	if n % u.head(primos) == 0:
		return u.head(primos)
	
	return alguem_divide(n, u.tail(primos))

def primes(n):
	
	print(f"n: {n}\n")
	
	if not f(n):
		return []
	
	print(alguem_divide(n, f(n+1)))
	
	if alguem_divide(n, f(n+1)):
		return [alguem_divide(n,f(n+1))] + primes(int (n / u.head(f(n+1))))
	return []
	
	
def main():
	
	print(f(8))
	print(primes(8))
    

if __name__=="__main__":
    main()
