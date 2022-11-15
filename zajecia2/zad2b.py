def pomnozone(lista:list):

    for i in range(0,len(lista)):
        lista[i] = lista[i] * 2
        i += 1
    print(lista)

pomnozone([1,2,1,1,1])

def pomnozone_ii (lista:list):
    pomnoz = [(i*2) for i in lista]
    print(pomnoz)

pomnozone_ii([1,2,3])

