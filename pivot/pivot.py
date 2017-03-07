# coding: utf-8
# Pivot
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def pivot(numeros):
	aux = 0
	pos_meupivot = 0	
	if len(numeros) > 1:
		meu_pivot = numeros[0]
		for i in range(1,len(numeros)):
			meu_pivot = numeros[pos_meupivot]
			if meu_pivot > numeros[i]:
				#print numeros
				#numeros[pos_meupivot], numeros[i] = numeros[i], numeros[pos_meupivot]
				aux = numeros.pop(i)
				numeros.insert(pos_meupivot, aux)
				pos_meupivot += 1


numeros = [6, 4, 4, 4, 4, 4, 4]
pivot(numeros)
assert numeros == [4, 4, 4, 4, 4, 4, 6]

numeros = [-1, 4, 4, 4, 4, 4, 4]
pivot(numeros)
assert numeros == [-1,4, 4, 4, 4, 4, 4]

numeros = [1,0,0]
pivot(numeros)
assert numeros == [0,0,1]

numeros = [-10,-1,-1,-5,-12]
pivot(numeros)
assert numeros == [-12,-10, -1, -1, -5]

numeros = []
pivot(numeros)
assert numeros == []

numeros = [1,0]
pivot(numeros)
assert numeros == [0,1]

numeros = [5, 5, 6, 7, 4, 4]
pivot(numeros)
assert numeros == [4,4,5,5,6,7]

numeros = [5,4,3,2,1]
pivot(numeros)
assert numeros == [4,3,2,1,5]

numeros = [4,4,2,2]
pivot(numeros)
assert numeros == [2,2,4,4]

numeros = [2,2,4,4]
pivot(numeros)
assert numeros == [2,2,4,4]


