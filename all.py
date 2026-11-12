import utils as u


def all(lista):
    return list(filter(lambda x: x, lista)) == lista

def main():
    print(all([True, True, False]))


if __name__ == "__main__":
    main()
