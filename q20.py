import utils as u
from q14 import pertence


def strip(list1, list2):
    # print(list1)
    # print(list2)
    if not list1 or not list2: # ve se a lista está vazia
        return []
    
    if pertence(u.head(list1), list2):
        return strip(u.tail(list1), list2)
    else:
        return [u.head(list1)] + strip(u.tail(list1), list2)

def main():
    list1 = [1, 4, 2, 3]
    list2 = [2]
    print(strip(list1, list2))

if __name__=="__main__":
    main()
