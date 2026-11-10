import utils as u
from q21 import consoantList

def matches(dic, consoants):
	if not dic:
		return []
	
	if consoantList(u.head(dic), consoants):
		return [u.head(dic)] + matches(u.tail(dic), consoants)
		
	return matches(u.tail(dic), consoants)
	

def main():
    
    dic = ["arara", "arreio", "haskell", "vaca", "vacuo", "velho", "vermelho", "vicio"]
    
    print(matches(dic, "rr"))
    print(matches(dic, "vc"))

if __name__=="__main__":
    main()
