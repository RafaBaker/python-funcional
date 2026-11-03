def head(list):
    return list[0]

def tail(list):
    new_list = []
    for i in range(1, len(list)):
        new_list.append(list[i])
    return new_list

def init(list):
    new_list = []
    for i in range(0, len(list)-1):
        new_list.append(list[i])
    return new_list

def last(list):
    return list[len(list)-1]
