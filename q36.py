from q35 import pack
from utils import *


def len(data):
    if not data: return 0
    
    return 1 + len(tail(data))

def encode(data):
    
    
    return (list(map(freq_tupla, pack(data))))
    

def freq_tupla(data):
    return (len(data), head(data))

def main():
    
    print(encode("aaaabccaadeeee"))
    
    return 0

if __name__=="__main__":
    main()
