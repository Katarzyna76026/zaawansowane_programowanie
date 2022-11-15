def co_drugi(lista:list):
    for i in range(0,len(lista)):
        if (i%2 == 0):
            print(lista[i])
            i += 1

co_drugi([1,2,3,3,4,5,4,6,7,3])