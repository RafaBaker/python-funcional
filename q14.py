import utils as u


def pertence(x, list):
    if not list:
        return False
    elif u.head(list) == x:
        return True
    return pertence(x, u.tail(list))

def main():
    list = [1]
    x = 1
    y = 0

    print(pertence(x, list))
    print(pertence(y, list))

if __name__=="__main__":
    main()