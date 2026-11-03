import utils as u
    
def concatena(list1, list2):
	if list1:
		return u.head(list1) + concatena(u.tail(list1), list2)
	if list2:
		return u.head(list2) + concatena(list1, u.tail(list2))
	return 0
    
def main():
	list1 = [1, 5, 3]
	list2 = [4, 5, 6]
	
	print(list1+list2)
	print(concatena(list1, list2))

if __name__=="__main__":
    main()
