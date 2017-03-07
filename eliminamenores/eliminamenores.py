# coding: utf-8
# Elimina Menores
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def elimina_menores(num, lista):
	removidos = 0
	ficaram = []
	for i in range(len(lista)-1,-1,-1):
		if lista[i] < num:
			lista.remove(lista[i])
			removidos += 1
	return removidos 
lista1 = [100,200,300,400]
assert elimina_menores(100, lista1) == 0
assert lista1 == [100,200,300,400]

lista2 = [3,5,1,7,10,9]
assert elimina_menores(4, lista2) == 2
assert lista2 == [5,7,10,9]

