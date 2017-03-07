# coding: utf-8
# Aplicação Polinômios
# (C) 2016, Yovany Cunha / UFCG, Programação 1

import math

def aplica_polinomio(lista_polinomio,valor):
	soma = 0
	for i in range(len(lista_polinomio)):
		soma += lista_polinomio[i] * pow(valor,i)
	return soma


if __name__ == '__main__':
	#entrada = raw_input('')
	valor = 0
	while True:#entrada != 'fim':
		entrada = raw_input('')
		if entrada == 'fim': break
		if entrada[0] == 'p':
			entrada = entrada.split()
			print 'novo polinomio'
			lista_polinomio = []
			for l in range(1,len(entrada)):
				lista_polinomio.append(int(entrada[l]))
			valor = int(raw_input(''))
			print aplica_polinomio(lista_polinomio,valor)

		else:
			valor = int(entrada)
			print aplica_polinomio(lista_polinomio,valor)

