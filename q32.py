from utils import *


def checa_linha(dama, outra_dama):
    return head(dama) == head(outra_dama)

def checa_coluna(dama, outra_dama):
    return last(dama) == last(outra_dama)

def checa_diagonal(dama, outra_dama):
    # print(abs(head(dama) - last(dama)))
    return abs(head(dama) - last(dama)) == abs(head(outra_dama) - last(outra_dama))

def ataca(dama, posicao):
    
    if not posicao:
        return False
    
    outra_dama = head(posicao)
    # print(outra_dama)
    
    return True if checa_linha(dama, outra_dama) or checa_coluna(dama, outra_dama) or checa_diagonal(dama, outra_dama) else ataca(dama, tail(posicao))

def main():
    
    # print(checa_linha((2,3), (2,6)))
    # print(checa_coluna((2,3), (2,6)))
    # print(checa_diagonal())
    
    # print(ataca((2, 3), [(2, 6), (5, 1)])) # True
    print(ataca((2, 3), [(1, 1), (4, 2)]))  # False
    
    return 0


if __name__=="__main__":
    main()