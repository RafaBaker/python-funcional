import utils as u


def f(list, n):
    # print(list)
    if not list: # ve se a lista está vazia
        return 0
    if u.head(list) > n:
        return 1 + f(u.tail(list), n)
    return f(u.tail(list), n)


def main():
    list = [1, -2, -3, -4, 6]
    print(f(list, -10))

if __name__=="__main__":
    main()
