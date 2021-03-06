def antidiagonal(matriz):
   if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
      return antidiagonal_aux(matriz, len(matriz), 0, 0)
   else:
      return -1

def antidiagonal_aux(matriz, largo, fila, suma):
   if (fila == largo):
      return suma
   else:
      return antidiagonal_aux(matriz, largo, fila + 1, suma + matriz[fila][-(fila + 1)])
