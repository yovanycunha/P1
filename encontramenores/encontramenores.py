# coding: utf-8
# Encontra Menores 
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def encontra_menores(num,lista):
	menor = 0
	outro_menor = 0
	count = 0
	aux = 0
	while count < len(lista):
		if lista[count] < num:
			menor = lista[count]
			return menor
			break
		count += 1
	if count == len(lista):
		return -1

lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
