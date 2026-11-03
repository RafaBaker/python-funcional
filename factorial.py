import utils as u

def factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*factorial(n-1)

def main():
    print(factorial(7))

if __name__=="__main__":
    main()
