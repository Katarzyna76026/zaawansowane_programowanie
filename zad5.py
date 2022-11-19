def type_hinting(lista: list, a: int) -> bool:

    if a in lista:
        return True
    else:
        return False
print(type_hinting([1,2,3],5))