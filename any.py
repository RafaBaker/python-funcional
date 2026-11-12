import utils as u


def any(lista):
    return list(filter(lambda x: x, lista)) != []

def main():
    print(any([False, False, False]))


if __name__ == "__main__":
    main()
