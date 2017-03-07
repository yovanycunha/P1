# coding: utf-8
# Junção Ordenada
# (C) 2016, Yovany Cunha / UFCG, Programação 1

def juncao_ordenada(lista1,lista2):
	k = 0
	i = 0
	ordenada = []
	if len(lista1) > len(lista2):
		while True:
			print ordenada
			if k == len(lista2) or i == len(lista1): break
			if lista2[k] > lista1[i]:
				ordenada.append(lista1[i])
				i += 1
			else:
				ordenada.append(lista2[k])
				k += 1
	return ordenada


l1 = [8, 11, 78, 79, 301, 302, 303,502,510]
l2 = [7, 8, 121, 305]
print juncao_ordenada(l1, l2)# == [7, 8, 8, 11, 78, 79, 121, 302, 511]
