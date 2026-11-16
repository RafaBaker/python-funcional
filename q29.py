def pyths(n):
    numeros = [x for x in range(1, n+1)]
    
    return [ (x, y, z) for x in numeros for y in numeros for z in numeros if (x*x)+(y*y)==(z*z) ]

def main():

    print(pyths(10))

if __name__ == "__main__":
    main() 