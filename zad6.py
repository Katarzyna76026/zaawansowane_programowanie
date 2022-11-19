import math

def listy(lista1: list,lista2: list):
    mylist = lista1.__add__(lista2)
    mylist = list(dict.fromkeys(mylist))
    for i in range (0,len(mylist)):
        mylist[i] = math.pow(mylist[i],3)
        i += 1
    print(mylist)
listy([1,2],[2,4])