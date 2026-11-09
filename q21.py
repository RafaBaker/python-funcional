import utils as u
from q14 import pertence
from q20 import strip


def consoantList(consoant, list):
    if not list:
        return
    
    return (consoant == "".join(strip(list, "aeiou")))

def main():
    
    print(strip("saude", "aeiou"))
    print(strip("saudade", "aeiou"))

    print(consoantList("sdd", "saude"))
    print(consoantList("sdd", "saudade"))


if __name__=="__main__":
    main()
