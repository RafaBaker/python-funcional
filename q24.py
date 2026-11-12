import utils as u
from q11 import ehPrimo


def alguem_divide(n, primos):
	
	# print("primos: ")
	# print(primos)
	
	
	if not primos: 
		return
	
	if n % u.head(primos) == 0:
		return u.head(primos)
	
	return alguem_divide(n, primos[1:])

def primes(n):
	
	if n <= 1:
		return []

	# print(alguem_divide(n, f(n+1)))
	divisor = alguem_divide(n, list(filter(ehPrimo, range(2, n + 1))))
	return [divisor] + primes(n // divisor)

def main():
	
	# print(f(8))
	print(primes(8))
	

if __name__=="__main__":
	main()
