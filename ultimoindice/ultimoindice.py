# coding: utf-8
# Último índice
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def ultimo_indice(num,lista):
	for i in range(len(lista)-1,-1,-1):
		if lista[i] == num:
			return i
	return -1
