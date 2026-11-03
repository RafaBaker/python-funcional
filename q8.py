import utils as u

def f(list):
    if (u.head(list) == 0):
        return 0
    if (u.head(list) < 0):
        return u.head(list)+f(u.tail(list))
    return f(u.tail(list))

def main():
    list = [1, 2, 3, -4 , 0]
    print(f(list))

if __name__=="__main__":
    main()
