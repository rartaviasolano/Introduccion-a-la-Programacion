def mult(lista):
    if isinstance(lista, list) and (lista != []):
        return mult_aux(lista, 0, len(lista), 1)
    else:
        return -1

def mult_aux(lista, indice, largo, resultado):
    if (indice == largo):
        return resultado
    else:
        return mult_aux(lista, indice + 1, largo, resultado * lista[indice])
