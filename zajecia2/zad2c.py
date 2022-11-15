def parzyste (lista:list):
    for i in range (0,len(lista)):
        if (lista[i] % 2 == 0):
            print(lista[i])
            i += 1

parzyste([2,6,9,10,5,14,22,2,3,2])