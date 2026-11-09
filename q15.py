import utils as u
from q14 import pertence


def concatena(list1, list2):
    if not list1 and not list2:
        return []
    elif list1:
        if pertence(u.head(list1), u.tail(list1)):
            return [] + concatena(u.tail(list1), list2)
        return [u.head(list1)] + concatena(u.tail(list1), list2)
    elif list2:
        if pertence(u.head(list2), u.tail(list2)):
            return [] + concatena(list1, u.tail(list2))
        return [u.head(list2)] + concatena(list1, u.tail(list2))
    return []

def main():
    list1 = [1, 1, 5, 3]
    list2 = [4, 5, 4, 6]
    
    print(list1+list2)
    print(concatena(list1, list2))

if __name__=="__main__":
    main()
