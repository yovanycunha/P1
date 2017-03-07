# coding: utf-8
# Pré-Vogais
# (C) 2016, Yovany Cunha / UFCG, Programação 1
import string

def pre_vogais(palavra):
	lista = []
	for i in range(1,len(palavra)):
		for l in ['A','E','I','O','U','a','e','i','o','u']:
			if l == palavra[i]:
				lista.append(string.lower(palavra[i-1]))
	
	for i in range(1,len(lista)):
		if lista[i-1] == lista[i]:
			lista.remove(lista[i-1])
	return lista

palavra = 'arara'
print pre_vogais(palavra)
