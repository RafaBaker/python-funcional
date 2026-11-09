import utils as u
from q13 import concatena
from q18 import invertelista


def geraPalindromo(list):
    # print(list)
    if not list: # ve se a lista está vazia
        return
    return concatena(list, invertelista(list))

def main():
    list = "abcd"
    print("".join(geraPalindromo(list)))

if __name__=="__main__":
    main()
