# coding: utf-8
# Filtra Lista
# (C) 2016, Yovany Cunha / UFCG, Programação 1


def filtra_lista(num, lista):
	retorno = [lista[0]]
	for i in range(1,len(lista)):
		if i % num == 0:
			retorno.append(lista[i])
	return retorno

lista1 = [0,1,2,3,4,5,6]
lista2 = [2,3,5,7,11,13,17]
assert filtra_lista(2, lista1) == [0,2,4,6]
assert filtra_lista(3, lista1) == [0,3,6]
assert filtra_lista(4, lista2) == [2,11]
assert filtra_lista(40, lista2) == [2]

