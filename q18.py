import utils as u
from q13 import concatena


def invertelista(list):
    # print(list)
    if not list: # ve se a lista está vazia
        return
    return concatena(invertelista() u.head(list))

def main():
    list = [1, -2, -3, -4, 6]
    print(invertelista(list))

if __name__=="__main__":
    main()
