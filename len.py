from functools import reduce

import utils as u


def f_len(lista):
    
    return reduce(lambda x, y: x+1, lista)


def main():
    print(f_len([True, True, False, 1]))


if __name__ == "__main__":
    main()
