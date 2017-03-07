#coding: utf-8
# Remove Menores
# (C) 2016, Yovany Cunha/UFCG, Programaçao I


def remove_menores(num, numeros):
	eliminados = 0
	for i in range(len(numeros)-1,-1,-1):
		if numeros[i] < num:
			numeros.pop(i)
			eliminados += 1
	return eliminados

lista = [1, 2, 3, 4, 5]
assert remove_menores(3, lista) == 2
assert lista == [3, 4, 5]


