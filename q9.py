import utils as u

def f(list, N):
    if (N==0):
        return 0
    if (u.head(list) < 0):
        return 1 + f(u.tail(list), N-1)
    if (u.head(list) >= 0):
        return 0 + f(u.tail(list), N-1)

def main():
    list = [1, -2, -3, -4]
    print(f(list,4))

if __name__=="__main__":
    main()
