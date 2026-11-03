import utils as u

def f(list):
    if not list: # ve se a lista está vazia
        return 0
    return 1 + f(u.tail(list))

def main():
    list = [1, -2, -3, -4, 6]
    print(f(list))

if __name__=="__main__":
    main()
